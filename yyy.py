from selenium import webdriver

# open a new chrome browser
driver = webdriver.Chrome("./chromedriver.exe")
# load the page at the given URL
driver.get("http://www.python.org")
assert "Python" in driver.title

driver.close()