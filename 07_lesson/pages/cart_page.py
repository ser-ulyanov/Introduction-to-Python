from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.NAME, "checkout")

    def proceed_to_checkout(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        button.click()
        return self

    def get_cart_items_count(self):

        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items)
