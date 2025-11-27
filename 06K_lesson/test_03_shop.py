from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
from selenium.webdriver.common.keys import Keys

def test_form():
    driver.get('https://www.saucedemo.com/')
    Username = driver.find_element(By.CSS_SELECTOR,'#user-name')
    Username.send_keys("standard_user", Keys.RETURN)
    Password= driver.find_element(By.CSS_SELECTOR,'#password')
    Password.send_keys("secret_sauce", Keys.RETURN)
    button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    button.click()
    waiter=WebDriverWait (driver, 50)



driver.quit()