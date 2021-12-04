from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from main_page import MainPage

driver = webdriver.Chrome(ChromeDriverManager().install())
main_page = MainPage(driver)
main_page.open()
assert "Python" in driver.title
main_page.search("pycon")
assert "No results found." not in main_page.page_source()
main_page.quit()

