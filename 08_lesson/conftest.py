import pytest
import requests
from config import BASE_URL, get_auth_token, get_headers


@pytest.fixture(scope="session")
def auth_token():
    """Фикстура для получения токена авторизации"""
    token = get_auth_token()
    assert token is not None, "Не удалось получить токен"
    print(f" Токен получен: {token[:20]}...")
    return token


@pytest.fixture
def headers(auth_token):
    """Фикстура для заголовков с токеном"""
    return get_headers()


@pytest.fixture
def create_project(headers):
    """Фикстура для создания проекта"""
    created_projects = []

    def _create_project(name):
        url = f"{BASE_URL}/api-v2/projects"
        payload = {"name": name}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 201:
            project_id = response.json().get("id")
            created_projects.append(project_id)
            return project_id, response
        return None, response

    yield _create_project

    # Очистка (можно добавить логирование)
    for project_id in created_projects:
        print(f" Проект {project_id} создан для теста")
