

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

# chrome_options.add_argument("--headless")
chrome_options = Options()
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
try:
    e6 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, ("Your profile")))
    )
    time.sleep(3)
    e6.click()
    time.sleep(3)
    print("clicked")
except:
    driver.quit


# cookies = driver.get_cookies()
# session = requests.Session()
# for cookie in cookies:
#     session.cookies.set(cookie['name'], cookie['value'])
# print(session.get("https://github.com/Chr0110?tab=repositories", ).text)