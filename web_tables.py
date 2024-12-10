from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")
driver.maximize_window()

addButton = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[1]/span[1]/button").click()
time.sleep(10)

input_firstName = driver.find_element(By.ID,"firstname").send_keys("Rival")
input_lastName = driver.find_element(By.ID,"lastname").send_keys("Muhammad")
input_email = driver.find_element(By.ID,"email").send_keys("rivalmuhammad@gmail.com")
input_age = driver.find_element(By.ID,"age").send_keys("25 Tahun")
input_salary = driver.find_element(By.ID,"salary").send_keys("5,000,000,000,000,000,000,000,000")
input_deparment = driver.find_element(By.ID,"deparment").send_keys("Technology")
buttonLogin = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(10)

#'REGISTRATION FORM - DELETE USER
deleteUser = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[2]/table/tbody/tr[1]/td[7]/a[2]").click()
time.sleep(10)

# #REGISTRATION FORM - EDIT USER
editUser = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[2]/table/tbody/tr[1]/td[7]/a[1]").click()
time.sleep(10)
#' firstName = driver.find_element(By.XPATH,"(//input[@id='firstname'])[2]")
# firstName.send_keys("All")
# time.sleep(10)
# lastName = driver.find_element(By.ID,"lastname").send_keys("Aulia")
# email = driver.find_element(By.ID,"email").send_keys("aurelaulia@gmail.com")
# age = driver.find_element(By.ID,"age").send_keys("25 Tahun")
# salary = driver.find_element(By.ID,"salary").send_keys("5,000,000,000,000,000,000,000,000")
# deparment = driver.find_element(By.ID,"deparment").send_keys("Technology")
# Login = driver.find_element(By.XPATH,"//input[@type='submit']").click()
# time.sleep(10)