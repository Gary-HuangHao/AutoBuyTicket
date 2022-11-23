from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
# options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)

chrome = webdriver.Chrome('./chromedriver',chrome_options=options)
chrome.get("https://inline.app/booking/-MyeIq6w0WlGH5oRFcd_:inline-live-2/-MyeIqIyLZ5S6ZK_Cke5?language=zh-tw")

sleep(2)

datepicker = chrome.find_element(By.ID, "date-picker")
datepicker.send_keys(Keys.END)
chrome.execute_script("arguments[0].click();", datepicker)

calender = chrome.find_elements(By.CLASS_NAME,"sc-bczRLJ.hOwNPY")

for item in calender:
    print(item)