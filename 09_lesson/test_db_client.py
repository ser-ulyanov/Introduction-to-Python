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
    assert 'subject' in names, f"Таблица 'subject' не найдена! Найдены: {names}"
    print(f"✅ Таблицы в БД: {names}")


def test_create_subject():
    """Тест на добавление предмета."""
    # 1. Создаем данные
    subject_name = "Python autotest"
    create_subject(subject_name)

    # 2. Проверяем, что добавилось
    subjects = get_subjects()
    result = False
    for subject in subjects:
        if subject["subject_title"] == subject_name:
            result = True
            break

    # 3. Проверяем результат
    assert result is True, f"Предмет '{subject_name}' не найден в БД"
    print(f"✅ Предмет найден: {subject_name}")


def test_read():
    """Тест на чтение данных из таблицы."""
    with db.connect() as connection:
        result = connection.execute(text("SELECT subject_title FROM subject"))
        rows = result.mappings().all()

        # Проверяем, что таблица не пуста
        assert len(rows) > 0, "Таблица subject пуста! Нет данных для чтения."

        row1 = rows[0]
        print(f"Первая запись: title='{row1['subject_title']}'")

        # Проверяем, что есть данные
        assert row1['subject_title'] is not None, "subject_title не должен быть None"

        print("✅ test_read пройден!")


def test_update_subject():
    """Тест на обновление предмета."""
    # 1. Создаем
    old_name = "Python autotest"
    create_subject(old_name)

    # 2. Обновляем (удаляем старый, создаем новый с новым именем)
    new_name = "Python autotest updated"
    delete_subject_by_name(old_name)
    create_subject(new_name)

    # 3. Проверяем
    subjects = get_subjects()
    result = False
    for subject in subjects:
        if subject["subject_title"] == new_name:
            result = True
            break

    assert result is True, f"Обновленный предмет '{new_name}' не найден"
    print(f"✅ Предмет обновлен: {new_name}")


def test_delete_subject():
    """Тест DELETE: удаление существующего предмета из списка."""
    # 1. Получаем список всех предметов
    subjects = get_subjects()
    
    # Проверяем, что список не пуст
    assert len(subjects) > 0, "Таблица subject пуста! Сначала создайте данные через test_create_subject"
    print(f"✅ DELETE: Всего предметов в списке: {len(subjects)}")
    
    # 2. Берем ПЕРВЫЙ предмет из списка (или любой существующий)
    subject_name = subjects[0]["subject_title"]
    print(f"✅ DELETE: Выбран предмет для удаления: '{subject_name}'")
    
    # 3. Удаляем выбранный предмет
    delete_subject_by_name(subject_name)
    
    # 4. Проверяем, что удалился
    subjects_after = get_subjects()
    found = False
    for subject in subjects_after:
        if subject["subject_title"] == subject_name:
            found = True
            break
    
    assert found is False, f"Предмет '{subject_name}' не удален!"
    print(f"✅ DELETE: Предмет '{subject_name}' успешно удален")
    print(f"✅ DELETE: Осталось предметов: {len(subjects_after)}")
    print("✅ test_delete_subject пройден!")


def test_get_subjects():
    """Тест на получение списка предметов."""
    # 1. Создаем тестовую запись
    name = "Test list subject"
    create_subject(name)

    # 2. Получаем список
    subjects = get_subjects()
    print(f"Всего предметов: {len(subjects)}")

    # 3. Проверяем, что наша запись есть в списке
    found = False
    for subject in subjects:
        if subject["subject_title"] == name:
            found = True
            print(f"Найдено: title={subject['subject_title']}")
            break

    assert found, f"Созданный предмет '{name}' не найден в списке"
