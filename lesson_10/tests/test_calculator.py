import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.calculator_page import CalculatorPage


@allure.epic("Тестирование веб-приложений")
@allure.feature("Калькулятор")
@allure.story("Арифметические операции")
@allure.title("Проверка сложения чисел 7 и 8 с задержкой")
@allure.description("""
    Тест проверяет корректность работы калькулятора:
    1. Устанавливается задержка 45 секунд
    2. Выполняется сложение 7 + 8
    3. Проверяется результат (должен быть 15)
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "calculator", "positive")
def test_calculator(chrome: WebDriver) -> None:
    """Тест калькулятора"""
    calculator = open_calculator(chrome)
    set_delay(calculator, "45")
    perform_calculation(calculator)
    verify_result(calculator)


@allure.step("Открыть страницу калькулятора")
def open_calculator(driver: WebDriver) -> CalculatorPage:
    """Открывает страницу калькулятора"""
    calculator = CalculatorPage(driver)
    calculator.open()
    return calculator


@allure.step("Установить задержку {delay} секунд")
def set_delay(calculator: CalculatorPage, delay: str) -> None:
    """Устанавливает задержку"""
    calculator.set_delay(delay)


@allure.step("Выполнить вычисление 7 + 8")
def perform_calculation(calculator: CalculatorPage) -> None:
    """Выполняет вычисление"""
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")


@allure.step("Проверить результат вычисления")
def verify_result(calculator: CalculatorPage) -> None:
    """Проверяет результат вычисления"""
    result = calculator.get_result("15")
    assert result == "15", f"Ожидался результат '15', получен '{result}'"
