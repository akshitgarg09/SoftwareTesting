# Selecting from a dropdown

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/akshit/WebDrivers/chromedriver")

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

# identify dropdown with Select class
sel = Select(driver.find_element(by=By.XPATH, value="//select[@name='continents']"))
time.sleep(2)

# select from dropdown by select_by_visible_text() method
sel.select_by_visible_text("South America")
time.sleep(3)

# select from dropdown by select_by_index() method
sel.select_by_index(0)
time.sleep(3)

driver.quit()
