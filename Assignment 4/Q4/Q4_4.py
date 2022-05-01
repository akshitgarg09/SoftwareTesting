# Invoking JavaScript

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/akshit/WebDrivers/chromedriver")

driver.get("https://www.medium.com")

# Scroll Down
driver.execute_script("window.scrollTo(0, 2000)")
time.sleep(5)

js_script = '''
var name = prompt("Please enter your name:")
alert("Hey " + name)
'''
driver.execute_script(js_script)
time.sleep(15)

driver.quit()