import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class cartpage:
    def check(self,driver):
      checkout = driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def find_elements(self,driver):
      items = driver.find_elements(By.CSS_SELECTOR, "div.cart_item_label")
      content = "\n".join([item.text for item in items])
      return content 
    
    