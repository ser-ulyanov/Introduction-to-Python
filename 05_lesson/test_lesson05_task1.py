from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    original_url = "https://httpbin.org/"

    driver.get(original_url)

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML form")
    html_form_link.click()

    assert "/forms/post" in driver.current_url, \
        f"Ожидался URL, содержащий '/forms/post', получен {driver.current_url}"

    driver.back()

    assert driver.current_url == original_url, \
        f"Ожидался URL {original_url}, получен {driver.current_url}"

    driver.quit()
