from selenium import webdriver
from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_argument('--headless')

driver1 = webdriver.Chrome(options=option)
driver1.maximize_window()
url_tiket = ['https://www.tiket.com/', 'https://www.tokopedia.com/', 'https://orangsiber.com', 'https://idejongkok.com', 'https://kelasotomesyen.com/']
text = ['tiket.com', 'tokopedia.com', 'orangsiber.com', 'idejongkok.com', 'kelasotomeysen.com']
for prefix, url in zip(text, url_tiket):
    driver1.get(url)
    sleep(5)
    # title = driver1.title
    print(f'{prefix} - {driver1.title}')
driver1.close()

# Catatan web tiket dan tokopedia entah kenapa kalau di mode headless itu dia tidak bisa dibuka
# asumsi saya sepertinya web tersebut sudah ada pendeteksi bot agar tidak dapat di scrapping