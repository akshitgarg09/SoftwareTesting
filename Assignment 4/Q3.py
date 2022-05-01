from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/akshit/WebDrivers/chromedriver")

driver.get("https://medium.com")

print("Title is: ",driver.title)

driver.quit()