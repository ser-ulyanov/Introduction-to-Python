from pages.calculator_page import CalculatorPage


def test_calculator(chrome):

    calculator = CalculatorPage(chrome)

    calculator.open()

    calculator.set_delay("45")

    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    result = calculator.get_result()

    assert result == "15"
