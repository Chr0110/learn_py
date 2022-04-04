
from selenium import webdriver

PATH = "/Users/eradi-/Desktop/chrome_driver/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com")