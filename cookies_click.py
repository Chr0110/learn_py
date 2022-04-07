from argparse import Action
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
d=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=d, options=chrome_options)
driver.set_window_size(1000,1000)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookies = driver.find_element_by_id("bigCookie")
# cookies_count = driver.find_element_by_id("cookies")
# items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]
a = ActionChains(driver)


for i in range(5000):
    a.click(cookies)
a.perform()
while 1:
    pass