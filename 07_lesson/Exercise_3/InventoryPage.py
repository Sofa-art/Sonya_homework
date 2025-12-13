import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class inventorypage:
 def access (self,driver):
    backpack_add_button = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Backpack')]]//button").click()
    tshirt_add_button = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button").click()
    onesie_add_button = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Onesie')]]//button").click()
    cart= driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()