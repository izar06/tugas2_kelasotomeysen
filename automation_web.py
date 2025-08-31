from selenium import webdriver
# ====== Chrome ======
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_argument('--headless')
option.add_argument('--windows.size=1920, 1080')

driver1 = webdriver.Chrome(options=option)
driver1.maximize_window()
driver1.get('https://testapp.idejongkok.com')
driver1.save_screenshot('Bukti3.png')

title = driver1.title
print(title)
driver1.close()


# ====== Firefox =======
driver2 = webdriver.Firefox()
driver2.maximize_window()
driver2.get('https://testapp.idejongkok.com')
