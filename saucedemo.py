from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

sleep(2)
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
sleep(2)
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
sleep(2)
driver.find_element(By.ID, 'login-button').click()
sleep(2)
# driver.close()
title = driver.find_element(By.XPATH, "//span[@class = 'title']").text
print(title)
# title = driver.find_element(By.XPATH, "//span[@class = '']")

for i in range(1,7):
    driver.find_element(By.XPATH, f"//button[contains(text(), 'Add')][{i}]]").click()

