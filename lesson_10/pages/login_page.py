from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Класс для работы со страницей авторизации интернет-магазина SauceDemo
    Содержит методы для открытия страницы и выполнения входа в систему
    """
    def __init__(self, driver: WebDriver):
        """Инициализация страницы авторизации
        :param driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        # Локатор для ввода имени пользователя
        self.username_input = (By.ID, "user-name")
        # Локатор для ввода пароля
        self.password_input = (By.ID, "password")
        # Локатор для нажатия кнопки входа
        self.login_button = (By.ID, "login-button")

    def open(self):
        """Открытие страницы магазина"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username="standard_user", password="secret_sauce"):
        """Выполняет вход в систему с указанными учетными данными
        Заполняет поля логина и пароля, нажимает кнопку входа
        и ожидает перехода на страницу каталога товаров
        :param username: Имя пользователя (по умолчанию: "standard_user")
        :param password: Пароль (по умолчанию: "secret_sauce")
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        # Ввод имени пользователя
        self.driver.find_element(*self.password_input).send_keys(password)
        # Ввод пароля пользователя
        self.driver.find_element(*self.login_button).click()
        # Нажатие кнопки входа

        # Ожидание перехода на страницу инвентаря
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/inventory.html")
        )
