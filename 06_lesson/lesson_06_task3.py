from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get
    ("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Увеличенный таймаут до 45 секунд
    wait = WebDriverWait(driver, 45)
    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

    # Находим все картинки
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    if len(images) >= 4:
        print(images[2].get_attribute("src"))
    else:
        print(f"Ошибка: найдено только {len(images)} картинок")

finally:
    driver.quit()
