from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/login')

username_input = driver.find_element(By.XPATH,'//input[@id="username"]')
username_input.send_keys("tomsmith")

sleep(2)

password_input = driver.find_element(By.XPATH,'//input[@id="password"]')
password_input.send_keys("SuperSecretPassword!")

sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

sleep(2)

driver.quit()