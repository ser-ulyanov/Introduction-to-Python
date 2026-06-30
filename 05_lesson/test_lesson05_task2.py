from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    initial_url = "https://httpbin.org/forms/post"
    driver.get(initial_url)

    name_field = driver.find_element(By.NAME, "custname")

    test_name = "Иван Петров"
    name_field.send_keys(test_name)

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']"
    )
    submit_button.click()

    assert driver.current_url != initial_url, \
        f"URL не изменился, остался {driver.current_url}"

    driver.quit()
