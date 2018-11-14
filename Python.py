from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.python.org")
driver.implicitly_wait(5)
menu = driver.find_element_by_css_selector('.navigation menu #downloads')
time.sleep(5)
hidden_submenu=driver.find_element_by_css_selector('.subnav menu #downloads')
time.sleep(5)
ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

