import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = edge_driver_path = r"c:\Users\Саният\Desktop\Work\Edge\msedgedriver.exe"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")  
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    
    pole_z = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert pole_z == "alert py-2 alert-danger"

    # Проверка подсветки остальных полей
    poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
    for pole in poles:
        pole_class = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
        assert pole_class == "alert py-2 alert-success"

    driver.quit()