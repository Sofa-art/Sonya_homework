from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class mainpage:

  def __init__(self, driver): 
     """
     Фикстура для инициализации работы драйвера, Открывает страницу калькулятора
     """
     self.driver = driver
     self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
     self.driver.implicitly_wait(4)
     self.driver.maximize_window()

  @allure.step("Установка задержки {delay} секунд")
  def set_delay (self, delay):
      """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
      """
      text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
      text_input.clear()
      text_input.send_keys(str(delay))
    
   
    
  @allure.step("Нажатие кнопок калькулятора по очереди")
  def button(self):
      """
        Нажимает на несколько кнопок калькулятора по очереди.
        :param buttons: button_7, button_plus, button_8, button_equals, 
        которые нужно нажать.
      """
      button_7=self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
      button_plus=self.driver.find_element (By.XPATH, '//span[text()="+"]').click()
      button_8=self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
      button_equals=self.driver.find_element(By.XPATH, '//span[text()="="]').click()
      
      """
        Ожидает появления ожидаемого результата на экране калькулятора.
      """
      waiter=WebDriverWait (self.driver, 50)
      waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))
    
  @allure.step("Получение результата с экрана калькулятора и сравнение результата")
  def get_result(self)->str:
      """
      Возвращает текущий результат с экрана калькулятора.
      :return: str — текст результата на экране калькулятора.
      """
      result=self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
      print(result)
      return result