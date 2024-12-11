from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/login.php")
driver.maximize_window()

#Login as User
email = driver.find_element(By.ID,"email").send_keys("rivalms@gmail.com")
password = driver.find_element(By.ID,"password").send_keys("Abc12345")
loginButton = driver.find_element(By.XPATH,"//input[@type='submit']")
time.sleep(10)
driver.quit()