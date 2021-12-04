from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from main_page import MainPage

#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element(By.NAME, "q")
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.quit()

driver = webdriver.Chrome(ChromeDriverManager().install())
main_page = MainPage(driver)
main_page.open()
assert "Python" in driver.title
main_page.search("pycon")
assert "No results found." not in main_page.page_source()
main_page.quit()

