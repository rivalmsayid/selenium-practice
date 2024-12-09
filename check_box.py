from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/check-box.php")

MainLevel = driver.find_element(By.XPATH,"(//input[@id='c_io_4'])[1]").click()
time.sleep(10)

driver.quit()