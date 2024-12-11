from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/upload-download.php")
driver.maximize_window()

Download = driver.find_element(By.ID,"downloadButton").click()
time.sleep(10)

uploadFile = driver.find_element(By.ID,"uploadFile").send_keys("C:/Users/ASUS/Downloads/sampleFile.jpeg")
time.sleep(10)
driver.quit()