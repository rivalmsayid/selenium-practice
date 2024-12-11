from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/dynamic-prop.php")
driver.maximize_window()

button1 = driver.find_element(By.ID,"colorChange").click()
time.sleep(10)
button2 = driver.find_element(By.ID,"visibleAfter").click()
time.sleep(10)