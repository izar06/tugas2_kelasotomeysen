from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep
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
print(title)
# Menampilkan modal add product
driver.find_element(By.XPATH, "//span[normalize-space(text())='Add Product']").click()
try:
    element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Add New Product')]"))).text
    # Title = driver.title
    print(element)
    print('Modal Tampil')
    # Input Product Name
    sleep(1)
    nama_barang = 'Iphone 23 Pro'
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(nama_barang)
    # Input price
    sleep(1)
    driver.find_element(By.XPATH, "//input[@type='number']").send_keys(100)
    #Input Stock
    sleep(1)
    driver.find_element(By.XPATH, "(//input[@type='number'])[2]").send_keys(1000)
    #Click Category
    sleep(1)
    driver.find_element(By.XPATH, "//select[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500']").click()
    #Pilih Category
    sleep(1)
    driver.find_element(By.XPATH, "//option[@value='Computers']").click()
    # Isi Description
    sleep(1)
    driver.find_element(By.XPATH, "//textarea[@class='w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500']").send_keys('Test bang')
    # Click Add Product
    sleep(1)
    driver.find_element(By.XPATH, "//button[@class='flex-1 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors']").click()
    # driver.close()
except TimeoutException:
    print('Modal gk muncul om')
    pass

sleep(2)
validasi = driver.find_element(By.XPATH, f"//div[contains(text(), '{nama_barang}')]").text
print(validasi)
sleep(1)
driver.close()
