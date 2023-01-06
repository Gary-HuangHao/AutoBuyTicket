from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class lnline:
    def __init__(self) -> None:
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.chrome = webdriver.Chrome(
            './helper/chromedriver', chrome_options=self.options)
        # self.chrome.get(
        #     "https://inline.app/booking/-MyeIq6w0WlGH5oRFcd_:inline-live-2/-MyeIqIyLZ5S6ZK_Cke5?language=zh-tw")
        self.chrome.get(
            "https://inline.app/booking/-KW_p1r8kjOziXsHmha0:inline-live-thaitown/-KW_p1r8kjOziXsHmha1")

        self.start_crawler()

    def start_crawler(self) -> None:
        sleep(2)
        self.findelement_datepicker()

    def findelement_datepicker(self):
        datepicker = self.chrome.find_element(By.ID, "date-picker")
        datepicker.send_keys(Keys.END)
        self.chrome.execute_script("arguments[0].click();", datepicker)

        calender = self.chrome.find_elements(By.CLASS_NAME, "sc-bczRLJ.hOwNPY")
        for item in calender:
            isbooling = self.findelement_day(item)
            if (isbooling):
                print('訂位成功!!!')
                return

    def findelement_day(self, item) -> bool:
        try:
            dayElementCount = len(item.find_elements(By.XPATH, "*"))
            if (dayElementCount == 2):
                dayElement = item.find_elements(By.XPATH, "*")[1]
                dayElementClass = dayElement.get_attribute("class")
                dayElementClassStr = dayElementClass.replace(' ', '.')
                dayStatus = self.checkDayStatus(item, dayElementClassStr)
                if (dayStatus == 3):
                    # sleep(2)
                    # dayElement.send_keys(Keys.END)
                    self.chrome.execute_script(
                        "arguments[0].click();", dayElement)
                    return True
                else:
                    return False
            else:
                return False
        except NoSuchElementException:
            return False

    def checkDayStatus(self, item, classId) -> int:
        dayElement = item.find_elements(By.CLASS_NAME, classId)
        if (classId == 'sc-eCYdqJ.gBfQcQ') & (len(dayElement) > 0):
            return 1  # 橘色-最接近可訂位
        elif (classId == 'sc-eCYdqJ.bQpElv') & (len(dayElement) > 0):
            return 2  # 灰色-不可訂位
        elif (classId == 'sc-eCYdqJ.bcJLun') & (len(dayElement) > 0):
            return 3  # 白色-尚有空位
        else:
            return 0
