# test_projects.py
import pytest
import requests
from config import BASE_URL


class TestProjects:
    """Тесты для проектов Yougile"""

    # ============ POST /api-v2/projects ============

    def test_create_project_positive(self, headers):
        """Позитивный тест: создание проекта с валидными данными"""
        url = f"{BASE_URL}/api-v2/projects"
        payload = {
            "title": "Тестовый проект"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 201:
            print(f"Ответ сервера: {response.text}")

        assert response.status_code == 201, f"Ожидался 201, получен {
            response.status_code}"

        data = response.json()
        assert "id" in data, "В ответе нет id проекта"

    def test_create_project_negative_empty_title(self, headers):
        """Негативный тест: создание проекта с пустым названием"""
        url = f"{BASE_URL}/api-v2/projects"
        payload = {
            "title": ""  # Пустое название
        }

        response = requests.post(url, json=payload, headers=headers)

        # Ожидается ошибка 400
        assert response.status_code == 400, f"Ожидался 400, получен {
            response.status_code}"

        data = response.json()
        assert "error" in data or "message" in data, "Нет сообщения об ошибке"

    def test_create_project_negative_no_auth(self):
        """Негативный тест: создание без авторизации"""
        url = f"{BASE_URL}/api-v2/projects"
        payload = {
            "title": "Тестовый проект"
        }

        response = requests.post(url, json=payload)

        assert response.status_code == 401, f"Ожидался 401, получен {
            response.status_code}"

    # ============ PUT /api-v2/projects/{id} ============

    def test_update_project_positive(self, headers):
        """Позитивный тест: обновление проекта"""
        # Сначала создаем проект
        create_url = f"{BASE_URL}/api-v2/projects"
        create_payload = {
            "title": "Старое название"
        }
        create_response = requests.post(
            create_url, json=create_payload, headers=headers)

        if create_response.status_code != 201:
            print(f"Ошибка создания: {create_response.text}")
            pytest.skip("Не удалось создать проект для теста")

        project_id = create_response.json().get("id")

        # Теперь обновляем
        update_url = f"{BASE_URL}/api-v2/projects/{project_id}"
        update_payload = {
            "title": "Новое название"
        }

        response = requests.put(
            update_url, json=update_payload, headers=headers)

        if response.status_code != 200:
            print(f"Ошибка обновления: {response.text}")

        assert response.status_code == 200, f"Ожидался 200, получен {
            response.status_code}"
        data = response.json()
        assert data.get("id") == project_id

    def test_update_project_negative_wrong_id(self, headers):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        url = f"{BASE_URL}/api-v2/projects/{fake_id}"
        payload = {
            "title": "Новое название"
        }

        response = requests.put(url, json=payload, headers=headers)

        # Ожидается 404
        assert response.status_code == 404, f"Ожидался 404, получен {
            response.status_code}"

    def test_update_project_negative_empty_title(self, headers):
        """Негативный тест: обновление с пустым названием"""
        # Создаем проект
        create_url = f"{BASE_URL}/api-v2/projects"
        create_payload = {
            "title": "Тестовый проект"
        }
        create_response = requests.post(
            create_url, json=create_payload, headers=headers)

        if create_response.status_code != 201:
            pytest.skip("Не удалось создать проект для теста")

        project_id = create_response.json().get("id")

        # Пытаемся обновить с пустым названием
        update_url = f"{BASE_URL}/api-v2/projects/{project_id}"
        update_payload = {
            "title": ""
        }

        response = requests.put(
            update_url, json=update_payload, headers=headers)

        # Ожидается ошибка 400
        assert response.status_code == 400, f"Ожидался 400, получен {
            response.status_code}"

    # ============ GET /api-v2/projects/{id} ============

    def test_get_project_positive(self, headers):
        """Позитивный тест: получение проекта по ID"""
        # Создаем проект
        create_url = f"{BASE_URL}/api-v2/projects"
        create_payload = {
            "title": "Проект для получения"
        }
        create_response = requests.post(
            create_url, json=create_payload, headers=headers)

        if create_response.status_code != 201:
            print(f"Ошибка создания: {create_response.text}")
            pytest.skip("Не удалось создать проект для теста")

        project_id = create_response.json().get("id")

        # Получаем проект
        get_url = f"{BASE_URL}/api-v2/projects/{project_id}"
        response = requests.get(get_url, headers=headers)

        assert response.status_code == 200, f"Ожидался 200, получен {
            response.status_code}"
        data = response.json()
        assert data.get("id") == project_id
        assert "title" in data, "В ответе нет поля title"

    def test_get_project_negative_wrong_id(self, headers):
        """Негативный тест: получение несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        url = f"{BASE_URL}/api-v2/projects/{fake_id}"

        response = requests.get(url, headers=headers)

        # Ожидается 404
        assert response.status_code == 404, f"Ожидался 404, получен {
            response.status_code}"

    def test_get_project_negative_no_auth(self):
        """Негативный тест: получение проекта без авторизации"""
        fake_id = "11111111-1111-1111-1111-111111111111"
        url = f"{BASE_URL}/api-v2/projects/{fake_id}"

        response = requests.get(url)  # Без заголовков

        assert response.status_code == 401, f"Ожидался 401, получен {
            response.status_code}"
