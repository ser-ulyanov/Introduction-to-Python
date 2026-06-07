from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fillForm():
    driver = webdriver.Edge()
    waiter = WebDriverWait(driver, 40)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    phone = driver.find_element(By.NAME, "phone")
    phone.send_keys("+7985899998787")

    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.send_keys("")

    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job_position = driver.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")

    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    submit_button.click()

    waiter.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#zip-code.alert-danger"))
    )

    assert driver.find_element(
        By.CSS_SELECTOR, "#zip-code.alert-danger").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#first-name.alert-success").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#last-name.alert-success").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#address.alert-success").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#e-mail.alert-success").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#phone.alert-success").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#city.alert-success").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#country.alert-success").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#job-position.alert-success").is_displayed()
    assert driver.find_element(
        By.CSS_SELECTOR, "#company.alert-success").is_displayed()

    driver.quit()
