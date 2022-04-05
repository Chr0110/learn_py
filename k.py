from tkinter import E
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


d=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=d)
driver.set_window_size(1000,1000)
driver.get('https://github.com')
e1 = driver.find_element_by_css_selector('.d-inline-block').click()
e2 = driver.find_element_by_link_text("Sign in →").click()
e3 = driver.find_element_by_id('login_field')
e3.send_keys("Chr0110")
e4 = driver.find_element_by_id('password')
e4.send_keys("MehdiGithub@123")
e4 = driver.find_element_by_css_selector('.btn-primary').click()
e5 = driver.find_element_by_css_selector('.avatar-small').click()
driver.implicitly_wait(30)
e6 = driver.find_element_by_link_text("Your profile").click()
while 1:
    sleep(3)
