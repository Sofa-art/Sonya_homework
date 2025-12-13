import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class autopage:
     
 def __init__(self, driver): 
    self.driver = driver
    self.driver.get("https://www.saucedemo.com/")
    self.driver.implicitly_wait(4)
    self.driver.maximize_window()

 def entry (self):
    Username = self.driver.find_element(By.CSS_SELECTOR,'#user-name')
    Username.send_keys("standard_user", Keys.RETURN)
    Password= self.driver.find_element(By.CSS_SELECTOR,'#password')
    Password.send_keys("secret_sauce", Keys.RETURN)
    button = self.driver.find_element(By.CSS_SELECTOR, "#login-button")
    button.click()
    waiter=WebDriverWait (self.driver, 50)