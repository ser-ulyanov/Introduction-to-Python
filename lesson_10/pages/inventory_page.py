from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Класс для работы со страницей каталога товаров"""

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы каталога товаров
        :param driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver

    def add_items_to_cart(self) -> None:
        """
        Добавление товаров в корзину
        Добавляет три товара: Backpack, Bolt T-Shirt, Onesie
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def view_cart(self) -> None:
        """
        Переход в корзину
        Нажимает на иконку корзины для перехода к просмотру добавленных товаров
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container > a"
        ).click()
