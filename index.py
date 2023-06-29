
from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('your url')
driver.maximize_window()

# Login screen example
username = driver.find_element(By.ID, 'username').send_keys('your username')
password = driver.find_element(By.ID, 'password').send_keys('your password')


driver.find_element(By.ID, 'submit').click()
