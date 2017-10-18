from time import sleep
from page_object.BasePage import *
from selenium.webdriver.common.by import By
from page_object.SlicesPage import SlicesPage

class AnalyticPage(Page):
    #多维分析
    analytic_loc=(By.CSS_SELECTOR,"#main-header > span:nth-child(1) > span > a:nth-child(2)")
    #日期
    timeanalytic_loc=(By.CSS_SELECTOR,".time-picker-format.relative.iblock.height-100.line-height14")
    #添加维度
    addwslices_loc=(By.XPATH,"//*[text()='页面名称']")
    addchoiceslices_loc=(By.CSS_SELECTOR,".ant-popover-inner > div > div > div > button:nth-child(2)")
    #执行查询
    doslices_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-success.font14.center-of-relative")
    #切换单选框
    changeanalytic_loc=(By.CSS_SELECTOR,".itblock.alignright.line-height26 > i.sugoicon.sugo-tab.font16.pointer.mg1r.grey-at-first.iblock-force")
    #选择总记录数
    allanalytic_loc=(By.XPATH,"//*[text()='总记录数']")



    #多维分析查询验证
    def analytic_action1(self):
        sleep(1)
        self.type_click(*self.analytic_loc)
        sleep(1)
        self.type_click(*self.timeanalytic_loc)
        sleep(1)
        self.time_type('2017-07-16 00:00:00','2017-07-17 00:00:00')
        sleep(1)
        self.type_click(*self.addwslices_loc)
        sleep(1)
        self.type_click(*self.addchoiceslices_loc)
        self.type_click(*self.changeanalytic_loc)
        self.type_click(*self.allanalytic_loc)
        sleep(1)
        self.type_click(*self.doslices_loc)


    assert1_loc=(By.CSS_SELECTOR,".ant-table-body > table > tbody > tr:nth-child(2) > td:nth-child(1) > span.elli.itblock")
    assert2_loc=(By.CSS_SELECTOR,".ant-table-body > table > tbody > tr:nth-child(2) > td:nth-child(2) > span")
    def type_assert1(self):
        return self.find_element(*self.assert1_loc).text

    def type_assert2(self):
        return self.find_element(*self.assert2_loc).text