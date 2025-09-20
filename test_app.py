from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep

def test_login():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.get('https://testapp.idejongkok.com/')
    driver.maximize_window()
    # Input Email
    driver.find_element(By.XPATH, "//input[@placeholder = 'Enter your email']").send_keys('izar.anam22@gmail.com')
    # Input Password
    driver.find_element(By.XPATH, "//input[@placeholder = 'Enter your password']").send_keys('!Qwe1234')
    # Click Login
    driver.find_element(By.XPATH, "//span[contains(text(), 'Sign')]").click()
    # Cetak title halaman utaman
    title = driver.find_element(By.XPATH, "//h2[contains(text(), 'Product')]").text
    
    assert title == 'Product Inventory'
    
    driver.close()

# jika ingin menggunakan pytest nama file harus ada nama test / test_