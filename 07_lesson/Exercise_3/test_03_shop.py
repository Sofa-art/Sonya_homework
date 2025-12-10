import pytest
from selenium import webdriver
from AutoPage import autopage
from InventoryPage import inventorypage
from CartPage import cartpage
from Checkout import checkout


def test_shop():
    driver = webdriver.Firefox()
    auto_page = autopage(driver)
    auto_page.entry()
    inventory_page = inventorypage()
    inventory_page.access(driver)
    cart_page = cartpage()
    cart_page.check(driver)
    cart_page.find_elements(driver)
    checkout_page = checkout()
    checkout_page.form(driver)
    checkout_page.button(driver)
    checkout_page.total(driver)
    res = checkout_page.total (driver)
    assert res == 58.29
    driver.quit()