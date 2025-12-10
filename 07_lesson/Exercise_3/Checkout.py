import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class checkout:
    def form (self, driver):
       driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Саният")
       driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Леонова")
       driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("187112")
    
    def button(self, driver):
       continue_button = driver.find_element(By.ID, "continue").click()
    
    def total(self,driver):
       total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
       total_cost_value = float(total_cost.split("$")[1])
       return total_cost_value
    