from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

d=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=d)
#driver.minimize_window()
driver.set_window_size(1000,1000)
driver.get('https://github.com/Chr0110')
while 1:
    sleep(3)