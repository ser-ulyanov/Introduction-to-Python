from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс для работы со страницей оформления заказа"""

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы оформления заказа
        :param driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        # Локаторы для полей ввода информации о покупателе
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        # Локатор для кнопки продолжения
        self.continue_button = (By.ID, "continue")
        # Локатор для отображения итоговой суммы
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_customer_info(
            self, first_name: str, last_name: str, postal_code: str
            ) -> "CheckoutPage":
        """
        Заполнение информации о клиенте
        :param first_name: Имя покупателя
        :param last_name: Фамилия покупателя
        :param postal_code: Почтовый индекс
        :return: Экземпляр класса CheckoutPage для цепочки вызовов
        """
        self.driver.find_element(
            *self.first_name_input).send_keys(first_name)
        self.driver.find_element(
            *self.last_name_input).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_input).send_keys(postal_code)
        return self

    def continue_to_overview(self) -> "CheckoutPage":
        """
        Продолжить к обзору заказа
        Нажимает кнопку "Continue" для перехода к странице обзора заказа
        :return: Экземпляр класса CheckoutPage для цепочки вызовов
        """
        self.driver.find_element(*self.continue_button).click()
        return self

    def get_total_price(self) -> str:
        """
        Получение общей стоимости заказа
        Ожидает появления элемента с итоговой суммой и возвращает её
        :return: Строка с итоговой суммой (например: "$58.29")
        """
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.total_label)
        )
        total_element = self.driver.find_element(*self.total_label)
        total_text = total_element.text
        return total_text.replace("Total: ", "")
