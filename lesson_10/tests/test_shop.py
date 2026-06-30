import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.epic("Тестирование интернет-магазина")
@allure.feature("Оформление заказа через личный кабинет")
@allure.story("Добавление товара в корзину")
@allure.title("Тест проверки оформления заказа в интернет-магазине")
@allure.description("""
    Тест проверки оформления заказа в интернет-магазине:
    1. Открыть сайт магазина
    2. Авторизоваться как standard_user
    3. Добавить товары: Backpack, Bolt T-Shirt, Onesie
    4. Перейти в корзину
    5. Нажать Checkout
    6. Заполнить форму (Имя, Фамилия, Индекс)
    7. Проверить итоговую сумму $58.29
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "internet-shop", "positive")
def test_shop_checkout_total(firefox):
    with allure.step("Вход на странице авторизации браузера firefox"):
        login_page = LoginPage(firefox)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(firefox)
        inventory_page.add_items_to_cart()

    with allure.step("Перейти в корзину"):
        inventory_page.view_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart_page = CartPage(firefox)
        cart_page.proceed_to_checkout()

    with allure.step("Заполнить информацию о покупателе"):
        checkout_page = CheckoutPage(firefox)
        checkout_page.fill_customer_info("Иван", "Петров", "628200")

    with allure.step("Продолжить к обзору заказа"):
        checkout_page.continue_to_overview()

    with allure.step("Проверить итоговую сумму заказа"):
        total_text = checkout_page.get_total_price()
        assert total_text == "$58.29", (f"Ожидалась итоговая сумма $58.29, получена {total_text}")
