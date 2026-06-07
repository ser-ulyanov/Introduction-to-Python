from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Шаг 1: Перейдите на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Шаг 2: Укажите в поле ввода текст SkyPro
    # Ожидаем, пока поле ввода станет доступным
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    # Шаг 3: Нажмите на синюю кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Шаг 4: Получите текст кнопки и выведите в консоль
    # Ожидаем, пока текст кнопки изменится на "SkyPro"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    # Получаем текст измененной кнопки
    button_text = driver.find_element(By.ID, "updatingButton").text
    print(button_text)  # Выведет "SkyPro"

finally:
    driver.quit()
