from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import datetime
options = Options()
# options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)

chrome = webdriver.Chrome('./chromedriver',chrome_options=options)
chrome.get("https://inline.app/booking/-MyeIq6w0WlGH5oRFcd_:inline-live-2/-MyeIqIyLZ5S6ZK_Cke5?language=zh-tw")#酒灑


sleep(2)

datepicker = chrome.find_element(By.ID, "date-picker")
datepicker.send_keys(Keys.END)
chrome.execute_script("arguments[0].click();", datepicker)

calender = chrome.find_elements(By.CLASS_NAME,"sc-bczRLJ.hOwNPY")
def ChooseTime():

    pass
def Check_Child_Element_Exists_By_ClassName(item):
    try:
      childElementLen =len(item.find_elements(By.XPATH,"*"))
      if(childElementLen == 2):
        childElement =item.find_elements(By.XPATH,"*")[1]
        
        #選日期
        # childElementClass = item.find_elements(By.CLASS_NAME,"sc-eCYdqJ.gBfQcQ")#橘色-最接近可訂位
        childElementClass = item.find_elements(By.CLASS_NAME,"sc-eCYdqJ.bQpElv")#灰色-不可訂位
        # childElementClass = item.find_elements(By.CLASS_NAME,"sc-eCYdqJ.bcJLun")#白色-尚有空位
        if(len(childElementClass)>0):
            elementStrDay = childElementClass[0].get_attribute("data-date")#取日期
            elementStrDayToDateTime = datetime.datetime.strptime(elementStrDay, "%Y-%m-%d").date()
            today = datetime.date.today()
            if elementStrDayToDateTime < today:
                return False
            else:
                ChooseTime()
          
            print(childElementClass[0].text)
            return True
        
        #選時段
        return True
    except NoSuchElementException:
        return False
    return False

for item in calender:
    have = Check_Child_Element_Exists_By_ClassName(item)
    # print(item)


