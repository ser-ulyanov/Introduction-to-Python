from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fillForm():
    driver = webdriver.Firefox()
    waiter = WebDriverWait(driver, 30)

    driver.get("https://www.saucedemo.com/")

    login = driver.find_element(By.ID, "user-name")
    login.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container > a").click()

    driver.find_element(By.NAME, "checkout").click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Петров")

    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("628200")

    driver.find_element(By.ID, "continue").click()

    waiter.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label"))
    )

    total_element = driver.find_element(
        By.CSS_SELECTOR, ".summary_total_label"
        )
    total_text = total_element.text
    total = total_text.replace("Total: $", "")

    assert total == "58.29"

    driver.quit()
