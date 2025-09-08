from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.get('https://testapp.idejongkok.com/')
driver.maximize_window()
# sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder = 'Enter your email']").send_keys('izar.anam22@gmail.com')
# sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder = 'Enter your password']").send_keys('!Qwe1234')
# sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(), 'Sign')]").click()
title = driver.find_element(By.XPATH, "//h2[contains(text(), 'Product')]").text
print(title)
# sleep(1)
driver.close()