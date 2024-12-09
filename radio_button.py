from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/radio-button.php")

radioButton1 = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[1]/input").click()
time.sleep(10)

radioButton2 = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[3]/input").click()
time.sleep(10)