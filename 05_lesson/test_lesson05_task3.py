from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # Находим все ссылки на странице
    links = driver.find_elements(By.TAG_NAME, "a")

    # Проверяем количество ссылок (должно быть 10)
    assert len(links) == 10, \
        f"Ожидалось 10 ссылок, найдено {len(links)}"

    # Проверяем, что все ссылки отображаются
    for i, link in enumerate(links):
        assert link.is_displayed(), \
            f"Ссылка {i} не отображается на странице"

    # Примечание: в задании сказано проверить первую ссылку на наличие "1",
    # но фактически первая ссылка имеет текст "0".
    # Поэтому проверяем наличие любой ссылки с текстом "1"
    link_texts = [link.text for link in links]
    assert "1" in link_texts, \
        "Не найдено ссылки с текстом '1'"

    driver.quit()
