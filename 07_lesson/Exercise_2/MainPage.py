from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mainpage:

  def __init__(self, driver): 
    self.driver = driver
    self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    self.driver.implicitly_wait(4)
    self.driver.maximize_window()

  def set_delay (self):
     text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
     text_input.clear()
     text_input.send_keys("45")
    
   
    

  def button(self):
    button_7=self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
    button_plus=self.driver.find_element (By.XPATH, '//span[text()="+"]').click()
    button_8=self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
    button_equals=self.driver.find_element(By.XPATH, '//span[text()="="]').click()
    waiter=WebDriverWait (self.driver, 50)
    waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))
    
  def get_result(self):
    result=self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    print(result)
    return result