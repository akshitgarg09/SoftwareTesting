from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/akshit/WebDrivers/chromedriver")

driver.get("https://facebook.com")

email_element = driver.find_element(by=By.NAME,value="email")
password_element = driver.find_element(by=By.NAME,value="pass")

# Clear the fields and enter email and password
email_element.clear()
password_element.clear()
email_element.send_keys("mail@gmail.com")
password_element.send_keys("my_password")

# Clicking the login button
login_button = driver.find_element(by=By.NAME,value="login")
login_button.click()

time.sleep(15)
driver.quit()