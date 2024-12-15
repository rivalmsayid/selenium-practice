from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/modal-dialogs.php")
driver.maximize_window()

smallModal= driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/button[1]").click()
time.sleep(5)
close1 = driver.find_element(By.XPATH,"//*[@id='exampleModalSm']/div/div/div[3]/button").click()
time.sleep(10)

largeModal = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/button[2]").click()
time.sleep(5)
close2 = driver.find_element(By.XPATH,"//*[@id='exampleModalLg']/div/div/div[3]/button").click()
time.sleep(10)
driver.quit()