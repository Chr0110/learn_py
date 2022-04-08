from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.set_window_size(1000,1000)
driver.get("https://youtube.com")
e1 = driver.find_element_by_css_selector('#search-input.ytd-searchbox-spt input')
e1.send_keys("kendrick lamar")
driver.implicitly_wait(30)

driver.find_element_by_css_selector('#search-icon-legacy.ytd-searchbox yt-icon.ytd-searchbox').click()
driver.find_element_by_link_text("")
while 1:
    sleep (1)