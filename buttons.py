from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/buttons.php")
driver.maximize_window()

ClickMe = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/button[1]").click()
time.sleep(5)
RightClickMe = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/button[2]").click()
time.sleep(5)
DoubleClickMe = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/button[3]").click()
time.sleep(5)
