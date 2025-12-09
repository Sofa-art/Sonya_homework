import pytest
from selenium import webdriver
from MainPage import mainpage

def test_calc():
    driver = webdriver.Chrome()
    main_page = mainpage(driver)
    main_page.set_delay()
    main_page.button()
    main_page.get_result
    res = main_page.get_result()
    assert res == "15"
    

