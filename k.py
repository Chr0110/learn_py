from http import cookies
from tkinter import E
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import requests
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
d=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=d, options=chrome_options)
driver.set_window_size(1000,1000)
driver.get('https://github.com')
e1 = driver.find_element_by_css_selector('.d-inline-block').click()
e2 = driver.find_element_by_link_text("Sign in →").click()
e3 = driver.find_element_by_id('login_field')
e3.send_keys("Chr0110")
e4 = driver.find_element_by_id('password')
driver.implicitly_wait(30)
e4.send_keys("MehdiGithub@123")
e4 = driver.find_element_by_css_selector('.btn-primary').click()
e5 = driver.find_element_by_css_selector('.avatar-small').click()
driver.implicitly_wait(3000)
e6 = driver.find_element_by_link_text("Your profile").click()
time.sleep(3)
driver.quit()
# cookies = driver.get_cookies()
# session = requests.Session()
# for cookie in cookies:
#     session.cookies.set(cookie['name'], cookie['value'])
# print(session.get("https://github.com/Chr0110?tab=repositories", ).text)



# while 1:
#     sleep(3)

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.set_window_size(1000,1000)
# driver.get("https://youtube.com")
# e1 = driver.find_element_by_css_selector('#search-input.ytd-searchbox-spt input')
# e1.send_keys("pink floyd - time")
# driver.implicitly_wait(30)

# driver.find_element_by_css_selector('#search-icon-legacy.ytd-searchbox yt-icon.ytd-searchbox').click()

# time.sleep(3)
# driver.quit()