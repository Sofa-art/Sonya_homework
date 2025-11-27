import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

def test_form_validation():
    driver.get("https://www.saucedemo.com/")
    Username = driver.find_element(By.CSS_SELECTOR,'#user-name')
    Username.send_keys("standard_user", Keys.RETURN)
    Password= driver.find_element(By.CSS_SELECTOR,'#password')
    Password.send_keys("secret_sauce", Keys.RETURN)
    button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    button.click()
    waiter=WebDriverWait (driver, 50)
    backpack_add_button = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Backpack')]]//button").click()
    tshirt_add_button = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button").click()
    onesie_add_button = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Onesie')]]//button").click()
    cart= driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    checkout = driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Саният")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Леонова")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("187112")
    continue_button = driver.find_element(By.ID, "continue").click()
    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])
    assert total_cost_value == 58.29
    driver.quit()
    



