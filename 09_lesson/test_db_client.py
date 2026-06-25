from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


# ============ ФУНКЦИИ ДЛЯ РАБОТЫ С БД ============

def create_subject(name):
    """Создать новый предмет."""
    with db.connect() as connection:
        connection.execute(
            text("INSERT INTO subject(subject_title) VALUES (:name)"),
            {"name": name}
        )
        connection.commit()
        print(f"✅ Создан предмет: {name}")
        return name


def get_subjects():
    """Получить все предметы."""
    with db.connect() as connection:
        result = connection.execute(text("SELECT subject_title FROM subject"))
        return result.mappings().all()


def delete_subject_by_name(name):
    """Удалить предмет по названию."""
    with db.connect() as connection:
        connection.execute(
            text("DELETE FROM subject WHERE subject_title = :name"),
            {"name": name}
        )
        connection.commit()
        print(f"✅ Удален предмет: {name}")


def delete_all_subjects():
    """Удалить все предметы (для очистки)."""
    with db.connect() as connection:
        connection.execute(text("DELETE FROM subject"))
        connection.commit()
        print("✅ Удалены все предметы")


# ============ ТЕСТЫ ============

def test_db_connection():
    """Тест проверяет подключение к БД и наличие таблицы subject."""
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'subject' in names, f"Таблица 'subject' не найдена! Найдены: {
        names}"
    print(f"✅ Таблицы в БД: {names}")


def test_create_subject():
    """
    Тест CREATE: добавление предмета.
    ✅ Создает данные
    ✅ Удаляет данные после теста
    """
    subject_name = "Python autotest"

    # CREATE
    create_subject(subject_name)

    # READ - проверяем
    subjects = get_subjects()
    result = False
    for subject in subjects:
        if subject["subject_title"] == subject_name:
            result = True
            break

    assert result is True, f"Предмет '{subject_name}' не найден в БД"
    print(f"✅ CREATE: Предмет найден: {subject_name}")

    # DELETE - очистка после теста
    delete_subject_by_name(subject_name)
    print("✅ test_create_subject пройден!")


def test_read():
    """
    Тест READ: чтение данных.
    ✅ Создает данные
    ✅ Удаляет данные после теста
    """
    test_name = "Test Read Subject"

    # CREATE - создаем данные для чтения
    create_subject(test_name)

    # READ - читаем
    with db.connect() as connection:
        result = connection.execute(text("SELECT subject_title FROM subject"))
        rows = result.mappings().all()

        assert len(rows) > 0, "Таблица subject пуста!"

        found = False
        for row in rows:
            if row['subject_title'] == test_name:
                found = True
                break

        assert found is True, f"Предмет '{test_name}' не найден"
        print(f"✅ READ: Найден предмет: '{test_name}'")

    # DELETE - очистка после теста
    delete_subject_by_name(test_name)
    print("✅ test_read пройден!")


def test_update_subject():
    """
    Тест UPDATE: обновление предмета.
    ✅ Создает данные
    ✅ Удаляет данные после теста
    """
    old_name = "Python autotest"
    new_name = "Python autotest updated"

    # CREATE - создаем данные для обновления
    create_subject(old_name)

    # UPDATE - обновляем
    delete_subject_by_name(old_name)
    create_subject(new_name)

    # READ - проверяем
    subjects = get_subjects()
    old_found = False
    new_found = False

    for subject in subjects:
        if subject["subject_title"] == old_name:
            old_found = True
        if subject["subject_title"] == new_name:
            new_found = True

    assert old_found is False, f"Старый предмет '{
        old_name}' все еще существует!"
    assert new_found is True, f"Новый предмет '{new_name}' не найден!"
    print(f"✅ UPDATE: Старый удален, новый создан: {new_name}")

    # DELETE - очистка после теста
    delete_subject_by_name(new_name)
    print("✅ test_update_subject пройден!")


def test_delete_subject():
    """
    Тест DELETE: удаление предмета.
    ✅ Создает данные в рамках теста
    ✅ Удаляет данные после теста
    """
    # CREATE - создаем данные для удаления (в рамках теста)
    subject_name = "Python autotest for delete"
    create_subject(subject_name)

    # READ - проверяем, что создался
    subjects = get_subjects()
    found = False
    for subject in subjects:
        if subject["subject_title"] == subject_name:
            found = True
            break

    assert found is True, f"Предмет '{subject_name}' не создан"
    print(f"✅ DELETE: Предмет создан: {subject_name}")

    # DELETE - удаляем
    delete_subject_by_name(subject_name)

    # READ - проверяем, что удалился
    subjects_after = get_subjects()
    found = False
    for subject in subjects_after:
        if subject["subject_title"] == subject_name:
            found = True
            break

    assert found is False, f"Предмет '{subject_name}' не удален!"
    print(f"✅ DELETE: Предмет '{subject_name}' успешно удален")
    print("✅ test_delete_subject пройден!")


def test_get_subjects():
    """
    Тест GET: получение списка предметов.
    ✅ Создает данные
    ✅ Удаляет данные после теста
    """
    name = "Test list subject"

    # CREATE - создаем данные
    create_subject(name)

    # READ - получаем список
    subjects = get_subjects()
    print(f"✅ GET: Всего предметов: {len(subjects)}")

    # Проверяем
    found = False
    for subject in subjects:
        if subject["subject_title"] == name:
            found = True
            print(f"Найдено: title={subject['subject_title']}")
            break

    assert found, f"Созданный предмет '{name}' не найден в списке"
    print("✅ GET: Предмет найден в списке")

    # DELETE - очистка после теста
    delete_subject_by_name(name)
    print("✅ test_get_subjects пройден!")
