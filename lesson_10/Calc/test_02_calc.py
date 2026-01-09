import pytest
import allure
from selenium import webdriver
from ManePage import mainpage

@allure.description("Тест проверяет корректность работы калькулятора")
@allure.severity("normal")
@allure.title("Тестирование калькулятора на операцию +")
def test_calc():
    with allure.step(" Открытие браузера и страницы калькулятора"):
        driver = webdriver.Chrome()
        main_page = mainpage(driver)
    
    with allure.step("Установка задержки {delay} секунд"):
        main_page.set_delay(5)
    
    with allure.step("Нажатие кнопок 7, +, 8, ="):
        main_page.button()
    
    with allure.step("Получение результата"):
        main_page.get_result
    
    with allure.step("Проверка и сравнение результата"):
        res = main_page.get_result()
        assert res == "15"
