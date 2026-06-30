from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для работы со страницей калькулятора"""

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы калькулятора
        :param driver: WebDriver экземпляр
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result = (By.CSS_SELECTOR, ".screen")

    def open(self) -> "CalculatorPage":
        """
        Открывает страницу калькулятора
        :return: Экземпляр класса CalculatorPage для цепочки вызовов
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        return self

    def set_delay(self, value: str) -> "CalculatorPage":
        """
        Устанавливает значение задержки
        :param value: Значение задержки в секундах
        :return: Экземпляр класса CalculatorPage для цепочки вызовов
        """
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(value)
        return self

    def click_button(self, button: str) -> "CalculatorPage":
        """
        Нажимает кнопку с указанным текстом
        :param button: Текст на кнопке
        :return: Экземпляр класса CalculatorPage для цепочки вызовов
        """
        button_element = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((
                By.XPATH, f"//span[text()='{button}']"))
        )
        button_element.click()
        return self

    def get_result(self) -> str:
        """
        Получает результат вычисления
        :return: Текст результата
        """
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(self.result, "15")
        )
        return self.driver.find_element(*self.result).text
