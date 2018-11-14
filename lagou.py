from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver.exe")
# driver.get("http://www.lagou.com/")
# assert "拉勾" in driver.title

try:
    driver.implicitly_wait(5)
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")

    window_zhu = driver.current_window_handle
    driver.switch_to_window(window_zhu)
    while True:
        jobs_link=driver.find_element_by_css_selector()
finally:
