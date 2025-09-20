from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=option)
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
drag_element = driver.find_element(By.ID, 'draggable')
drop_element = driver.find_element(By.ID, 'droppable')

action = ActionChains(driver)

action.drag_and_drop(drag_element, drop_element)
action.perform()