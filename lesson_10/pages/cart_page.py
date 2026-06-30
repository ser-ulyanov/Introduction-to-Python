from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для работы со страницей корзины интернет-магазина"""
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы корзины
        :param driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        # Локатор для кнопки оформления заказа
        self.checkout_button = (By.NAME, "checkout")

    def proceed_to_checkout(self) -> "CartPage":
        """
        Переход к оформлению заказа
        Ожидает, пока кнопка "Checkout" станет кликабельной, и нажимает её
        :return: Экземпляр класса CartPage для цепочки вызовов
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        button.click()
        return self

    def get_cart_items_count(self) -> int:
        """
        Получение количества товаров в корзине
        :return: Количество товаров в виде целого числа
        """
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items)
