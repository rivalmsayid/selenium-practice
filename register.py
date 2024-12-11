from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/register.php")
driver.maximize_window()

#Register New User
firstName = driver.find_element(By.ID,"firstname").send_keys("rival")
lastName = driver.find_element(By.ID,"lastname").send_keys("muhammad")
userName = driver.find_element(By.ID,"username").send_keys("rivalms")
password = driver.find_element(By.ID,"password").send_keys("abcd12345")
buttonRegister = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(10)
driver.quit()