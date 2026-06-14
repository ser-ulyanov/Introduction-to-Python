from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_customer_info(
            self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_input).send_keys(postal_code)
        return self

    def continue_to_overview(self):
        self.driver.find_element(*self.continue_button).click()
        return self

    def get_total_price(self) -> str:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.total_label)
        )
        total_element = self.driver.find_element(*self.total_label)
        total_text = total_element.text

        return total_text.replace("Total: ", "")
