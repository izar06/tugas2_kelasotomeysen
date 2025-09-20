from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_login_positif():
    # Scenario/testcase : Login with correct email and password
    # Steps:
    # Buka Browsers
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Buka apps / URL
    driver.get('https://testapp.idejongkok.com')

    # Input Email
    driver.find_element(By.ID,'email').send_keys('uno.testing3@gmail.com')

    # Input Password
    driver.find_element(By.ID,'password').send_keys('123456789')

    # Click Sign in Button
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Masuk dashboard -> expected result
    profile = driver.find_element(By.XPATH, '//span[contains(text(),"Welcome, ")]').text
    
    assert profile == 'Welcome, uno.testing3@gmail.com'
    
    driver.close()

data_test_login = [('uno.testing3@gmail.co', '123456789', 'Invalid Email'),
                   ('uno.testing3@gmail.com', 'passwordsalah', 'Invalid Password')]
    
@pytest.mark.parametrize('email, password, errormsg', data_test_login)    
def test_login_negatif_1(email, password, errormsg):
    # Scenario/testcase : Login with incorrect email
    # Steps:
    # Buka Browsers
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Buka apps / URL
    driver.get('https://testapp.idejongkok.com')

    # Input Email
    driver.find_element(By.ID,'email').send_keys(email)

    # Input Password
    driver.find_element(By.ID,'password').send_keys(password)

    # Click Sign in Button
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Error -> expected result
    error_message = driver.find_element(By.XPATH, '//p[@class="text-red-600 text-sm"]').text 
    assert error_message == errormsg
    
    driver.close()
    
    
def test_login_negatif_2():
    # Scenario/testcase : Login with incorrect email
    # Steps:
    # Buka Browsers
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Buka apps / URL
    driver.get('https://testapp.idejongkok.com')

    # Input Email
    driver.find_element(By.ID,'email').send_keys('uno.testing3')

    # Input Password
    driver.find_element(By.ID,'password').send_keys('123456789')

    # Click Sign in Button
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()



    # Error -> expected result
    email_input = driver.find_element(By.ID,'email')
    
    error_notif = driver.execute_script('return arguments[0].validationMessage;', email_input)
    
    assert error_notif == "Please include an '@' in the email address. 'uno.testing3' is missing an '@'."
    
    driver.close()


