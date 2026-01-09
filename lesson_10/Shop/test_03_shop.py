import pytest
import allure
from selenium import webdriver
from AutoPage import autopage
from InventoryPage import inventorypage
from CartPage import cartpage
from Checkout import checkout

@allure.description("Тест проверяет корректность работы магазина")
@allure.severity("blocker")
@allure.title("Тестирование магазина на различные функции")
def test_shop():
    with allure.step("Открытие браузера и страницы магазина"):
        driver = webdriver.Firefox()
        auto_page = autopage(driver)

    with allure.step("Ввод логина и пароля в форму"):
        auto_page.entry()

    with allure.step("Добавление товара в корзину"):
        inventory_page = inventorypage()
        inventory_page.access(driver)

    with allure.step("Переход в корзину"):
        cart_page = cartpage()
        cart_page.check(driver)

    with allure.step("Проверка наличия товара в корзине"):
        cart_page.find_elements(driver)
    
    with allure.step("Ввод данных в форму"):
        checkout_page = checkout()
        checkout_page.form(driver)
    
    with allure.step("Нажатие на кнопку continue"):
        checkout_page.button(driver)
    
    with allure.step("Получение и сравнение итоговой суммы"):
        checkout_page.total(driver)
        res = checkout_page.total (driver)
        assert res == 58.29
        driver.quit()