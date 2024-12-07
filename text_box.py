from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
driver.maximize_window()

fullName = driver.find_element(By.ID,"fullname")
fullName.send_keys("Rival Muhammad Sayid")

email = driver.find_element(By.ID,"email")
email.send_keys("rivalms@gmail.com")

address = driver.find_element(By.ID,"address")
address.send_keys("Bandung Barat")

password = driver.find_element(By.ID,"password")
password.send_keys("12345")

submit = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(10)

driver.quit()