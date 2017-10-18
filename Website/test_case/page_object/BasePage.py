from time import sleep
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Page():#页类基础
    def __init__(self,driver):#初始化
        self.driver=driver
        self.base_url="http://192.168.0.220:8000"
        self.timeout=10
        sleep(1)
#打开不同子页面git
    def _open(self,url):
        url_=self.base_url+url
        print("Test page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url==url_ ,'Did not land on %s' %url_

    def open(self):
        self._open(self.url)
#元素定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

#实时时间封装
    def nowtime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")

    def wait(self):
        WebDriverWait(self.driver, 5, 0.1).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".ant-message-custom-content.ant-message-success>span")))



    #时间控件封装
    #左边时间框
    time2_loc=(By.CSS_SELECTOR,'.ant-calendar-picker-input.ant-input[placeholder="请选择日期"]')
    #点击获取光标
    time3_loc=(By.CSS_SELECTOR,".ant-calendar-input")
    #小确认按钮
    timeallsureanalytic_loc = (By.CSS_SELECTOR, ".ant-calendar-ok-btn")
    #右边时间框
    time4_loc=(By.CSS_SELECTOR,'.ant-calendar-picker-input.ant-input[placeholder="Start"]')
    #大确认框
    timesureanalytic_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.iblock.mg1r")

    def type_time2(self,*selector):
        for obj in self.driver.find_elements(*selector):
            if obj.is_displayed():
                obj.click()

    def type_time3(self,time):
        self.find_element(*self.time3_loc).click()
        self.find_element(*self.time3_loc).clear()
        self.find_element(*self.time3_loc).send_keys(time)
        self.find_element(*self.timeallsureanalytic_loc).click()

    def time_type(self,time1,time2):
        self.type_time2(*self.time2_loc)
        sleep(0.5)
        self.type_time3(time1)
        sleep(0.5)
        self.type_time2(*self.time4_loc)
        sleep(0.5)
        self.type_time3(time2)
        sleep(0.5)
        self.type_time2(*self.timesureanalytic_loc)

    def type_click(self,*loc):
        self.find_element(*loc).click()

    def type_click1(self,*loc):
        for obj in self.driver.find_elements(*loc):
            if obj.is_displayed():
                obj.click()

    def type_send(self,send_value,*loc):
        self.find_element(*loc).click()
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(send_value)




