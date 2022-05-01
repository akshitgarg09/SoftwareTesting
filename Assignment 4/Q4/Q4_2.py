# Writing dynamic XPath for lists demo

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/akshit/WebDrivers/chromedriver")

driver.get("https://www.medium.com")


# identify element with an attribute using xpath
elem = driver.find_element(by=By.XPATH,value="/html/body/div[6]/div[2]/div[1]/a/img")
print("Source attribute of element: ", elem.get_attribute("src"))

driver.quit()