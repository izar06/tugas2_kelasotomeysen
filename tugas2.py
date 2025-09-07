from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=option)
driver.get('https://testapp.idejongkok.com/')
sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder = 'Enter your email']").send_keys('izar.anam22@gmail.com')
driver.find_element(By.XPATH, "//input[@placeholder = 'Enter your password']").send_keys('!Qwe1234')
driver.find_element(By.XPATH, "//span[contains(text(), 'Sign')]").click()