from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/accordion.php")
driver.maximize_window()

clickDropdown1 = driver.find_element(By.XPATH,"//*[@id='headingTwentyOne']/button").click()
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

clickDropdown2 = driver.find_element(By.XPATH,"//*[@id='headingTwentyTwo']/button").click()
time.sleep(10)
clickDropdown3 = driver.find_element(By.XPATH,"//*[@id='headingTwentyThree']/button").click()
time.sleep(10)
driver.quit()