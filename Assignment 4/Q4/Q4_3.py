# Iterating lists

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/akshit/WebDrivers/chromedriver")

driver.get("https://www.medium.com")


# identify element with an attribute using xpath
elem = driver.find_elements(by=By.XPATH,value="/html/body/div[6]/div[3]/div[5]")
for val in elem:
    print(val.text)

driver.quit()