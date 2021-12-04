import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from main_page import MainPage


@pytest.fixture(scope='session')
def main_page():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    my_main_page = MainPage(driver)
    return my_main_page
