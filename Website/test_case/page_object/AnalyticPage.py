from time import sleep
from page_object.BasePage import *
from selenium.webdriver.common.by import By
from page_object.SlicesPage import SlicesPage

class AnalyticPage(Page):
    #多维分析
    analytic_loc=(By.CSS_SELECTOR,"#main-header > span:nth-child(1) > span > a:nth-child(2)")
    #日期
    timeanalytic_loc=(By.CSS_SELECTOR,".time-picker-format.relative.iblock.height-100.line-height14")
    #小日期1
    time1analytic_loc=(By.CSS_SELECTOR,'.ant-calendar-picker-input.ant-input[placeholder="请选择日期"]')
    #日期框
    timeallanalytic_loc=(By.CSS_SELECTOR,".ant-calendar-input")
    #小确认
    timeallsureanalytic_loc=(By.CSS_SELECTOR,".ant-calendar-ok-btn")
    #小日期框2
    time2analytic_loc=(By.CSS_SELECTOR,'.ant-calendar-picker-input.ant-input[placeholder="Start"]')
    #大确认框
    timesureanalytic_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.iblock.mg1r")
    #添加维度
    addwslices_loc=(By.XPATH,"//*[text()='页面名称']")
    addchoiceslices_loc=(By.CSS_SELECTOR,".ant-popover-inner > div > div > div > button:nth-child(2)")
    #执行查询
    doslices_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-success.font14.center-of-relative")
    #切换单选框
    changeanalytic_loc=(By.CSS_SELECTOR,".itblock.alignright.line-height26 > i.sugoicon.sugo-tab.font16.pointer.mg1r.grey-at-first.iblock-force")
    #选择总记录数
    allanalytic_loc=(By.XPATH,"//*[text()='总记录数']")

    def type_analytic(self):
        self.find_element(*self.analytic_loc).click()

    def type_timeanalytic(self):
        self.find_element(*self.timeanalytic_loc).click()

    def type_time1analytic(self):
        self.find_element(*self.time1analytic_loc).click()

    def type_timeallanalytic(self,):
        self.find_element(*self.timeallanalytic_loc).click()
        sleep(1)
        self.find_element(*self.timeallanalytic_loc).clear()

    def type_sendtime1analytic(self,time):
        self.find_element(*self.timeallanalytic_loc).send_keys(time)

    def type_timeallsureanalytic(self):
        self.find_element(*self.timeallsureanalytic_loc).click()

    def type_time2analytic(self):
        self.find_element(*self.time2analytic_loc).click()

    def type_sendtime2analytic(self,time2):
        self.find_element(*self.timeallanalytic_loc).send_keys(time2)

    def type_timesureanalytic(self):
        self.find_element(*self.timesureanalytic_loc).click()

    def type_addwslices(self):
        self.find_element(*self.addwslices_loc).click()

    def type_addchoiceslices(self):
        self.find_element(*self.addchoiceslices_loc).click()

    def type_changeanalytic(self):
        self.find_element(*self.changeanalytic_loc).click()

    def type_allanalytic(self):
        self.find_element(*self.allanalytic_loc).click()

    def type_doslices(self):
        self.find_element(*self.doslices_loc).click()

    #多维分析查询验证
    def analytic_action1(self,time1,time2):
        sleep(2)
        self.type_analytic()
        sleep(2)
        self.type_timeanalytic()
        sleep(1)
        self.type_time1analytic()
        sleep(1)
        self.type_timeallanalytic()
        sleep(1)
        self.type_sendtime1analytic(time1)
        self.type_timeallsureanalytic()
        sleep(1)
        self.type_time2analytic()
        sleep(1)
        self.type_timeallanalytic()
        sleep(1)
        self.type_sendtime1analytic(time2)
        self.type_timeallsureanalytic()
        sleep(1)
        self.type_timesureanalytic()
        sleep(1)
        self.type_addwslices()
        sleep(1)
        self.type_addchoiceslices()
        self.type_changeanalytic()
        self.type_allanalytic()
        sleep(2)
        self.type_doslices()

    assert1_loc=(By.CSS_SELECTOR,".ant-table-body > table > tbody > tr:nth-child(2) > td:nth-child(1) > span.elli.itblock")
    assert2_loc=(By.CSS_SELECTOR,".ant-table-body > table > tbody > tr:nth-child(2) > td:nth-child(2) > span")
    def type_assert1(self):
        return self.find_element(*self.assert1_loc).text

    def type_assert2(self):
        return self.find_element(*self.assert2_loc).text