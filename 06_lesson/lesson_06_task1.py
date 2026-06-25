from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "ajaxButton"))
)

button.click()

message = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)

print(message.text)

driver.quit()
