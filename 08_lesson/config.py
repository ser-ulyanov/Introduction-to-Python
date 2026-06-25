import requests

BASE_URL = "https://ru.yougile.com"
EMAIL = "fourth927@gmail.com"
PASSWORD = "binokiO412/"
COMPANY_ID = "40606289-9d96-43bf-bea1-1b70d3b872d8"

AUTH_TOKEN = "W2mc0C-ZQ5JACre0mazC8W-qPshkNQZ-fzo-NUjNt9zrNSI5uH3xfk1xn1oof+Ik"


def get_auth_token():
    """Возвращает токен авторизации"""
    return AUTH_TOKEN


def get_headers():
    """Возвращает заголовки с токеном"""
    return {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


# Функция для получения токена через API (если понадобится)
def get_auth_token_from_api():
    """Получение токена через API (если готовый не работает)"""
    url = f"{BASE_URL}/api-v2/auth/keys"
    payload = {
        "login": EMAIL,
        "password": PASSWORD,
        "companyId": COMPANY_ID
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get("key")
        else:
            print(f"Ошибка получения токена: {response.status_code}")
            return None
    except Exception as e:
        print(f"Исключение: {e}")
        return None


if __name__ == "__main__":
    # Проверяем
    token = get_auth_token()
    headers = get_headers()
    print(f"Токен: {token[:30]}...")
    print(f"Заголовки: {headers}")
