from time import sleep
from page_object.BasePage import Page
from selenium.webdriver.common.by import By

class RetentionPage(Page):
    #用户运营
    traffic_loc=(By.XPATH,'//*[text()="用户运营"]')
    retention1_loc=(By.XPATH,'//*[text()="留存分析"]')
    #主时间
    maintime_loc=(By.CSS_SELECTOR,"#retention > div > div.scroll-content.always-display-scrollbar > div.chart-container > div > div.pd3x.pd2y > div.mg2t > div.itblock > div.mg2b.height32 > div")
    #增加一个过滤条件
    addchoice_loc=(By.CSS_SELECTOR,"#retention > div > div.scroll-content.always-display-scrollbar > div.chart-container > div > div.pd3x.pd2y > div.mg2t > div.itblock > div.pd1t > span")
    #查询按钮
    check_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.mg2t.width120")
    #第一个条件框
    input1_loc=(By.CSS_SELECTOR,".mg1b > div:nth-child(1) > div.ant-select-lg.width120.inline.mg1r.ant-select.ant-select-enabled > div > div")
    find1_loc=(By.XPATH,'//*[text()="客户端事件时间"]')
    time1_loc=(By.CSS_SELECTOR,".mg1b > div:nth-child(1) > div.time-picker-format.relative.iblock.width200.height32.itblock.line-height18 > span")
    #左边时间框
    # time2_loc=(By.CSS_SELECTOR,'.ant-calendar-picker-input.ant-input[placeholder="请选择日期"]')
    # #点击获取光标
    # time3_loc=(By.CSS_SELECTOR,".ant-calendar-input")
    # #小确认按钮
    # timeallsureanalytic_loc = (By.CSS_SELECTOR, ".ant-calendar-ok-btn")
    # #右边时间框
    # time4_loc=(By.CSS_SELECTOR,'.ant-calendar-picker-input.ant-input[placeholder="Start"]')
    # #大确认框
    # timesureanalytic_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.iblock.mg1r")
    #第二个条件框
    input2_loc = (By.CSS_SELECTOR, ".mg1b > div:nth-child(2) > div.ant-select-lg.width120.inline.mg1r.ant-select.ant-select-enabled > div > div")
    #查找页面名称
    find2_loc=(By.XPATH,"//*[text()='浏览器名称']")
    input21_loc=(By.CSS_SELECTOR,".mg2t > div.itblock > div.mg1b > div:nth-child(2) > button")
    #查找中兴品牌列表页
    find3_loc=(By.XPATH,"//*[text()='Chrome']")
    #确认按钮
    surebutton_loc=(By.CSS_SELECTOR,".aligncenter.pd2b > button.ant-btn.ant-btn-primary")
    #第三个条件框
    input3_loc = (By.CSS_SELECTOR, ".mg1b > div:nth-child(3) > div.ant-select-lg.width120.inline.mg1r.ant-select.ant-select-enabled > div > div")
    #查找停留时长
    find4_loc = (By.XPATH, "//*[text()='停留时长']")
    input31_loc=(By.CSS_SELECTOR,".mg1b > div:nth-child(3) > div.ant-row.width200.itblock > div:nth-child(1) > input")
    input32_loc=(By.CSS_SELECTOR,".mg1b > div:nth-child(3) > div.ant-row.width200.itblock > div:nth-child(3) > input")
    #保存按钮
    savebutton1_loc=(By.CSS_SELECTOR,"#retention > div > div.scroll-content.always-display-scrollbar > div.chart-container > div > div.pd3x.mg2t > div > div.fright > button > span")
    #输入名称
    inputname_loc=(By.CSS_SELECTOR,".ant-tabs-content.ant-tabs-content-animated > div > div > div:nth-child(2) > input")
    #保存
    savebutton2_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.width-100")
    #功能留存
    retention2_loc=(By.CSS_SELECTOR,".pd3x.pd2y > div.width-100.mg1t > div.ant-radio-group.block.mg2b > label:nth-child(2)")
    #选择页面名称
    input4_loc=(By.CSS_SELECTOR,".pd3x.pd2y > div.width-100.mg1t > div:nth-child(2) > div:nth-child(2) > div.width-100.ant-select.ant-select-enabled > div")
    find5_loc=(By.XPATH,'//*[text()="Apple品牌列表页"]')
    input5_loc=(By.CSS_SELECTOR,".width-100.mg1t > div:nth-child(2) > div:nth-child(4) > div.width-100.ant-select.ant-select-enabled > div > div > div.ant-select-selection-selected-value")
    find51_loc=(By.XPATH,'//*[text()="停留"]')
    #自定义留存
    retention3_loc=(By.CSS_SELECTOR,".pd3x.pd2y > div.width-100.mg1t > div.ant-radio-group.block.mg2b > label:nth-child(3)")
    input6_loc=(By.CSS_SELECTOR,".pd3x.pd2y > div.width-100.mg1t > div.iblock.mg1l > div:nth-child(3) > div.width-100.ant-select.ant-select-enabled > div > div")
    find6_loc=(By.XPATH,"//*[text()='手机概述']")
    #选择排除
    input7_loc=(By.CSS_SELECTOR,".pd3x.pd2y > div.mg2t > div.itblock > div.mg1b > div:nth-child(3) > div.ant-select-lg.width100.mg1r.inline.ant-select.ant-select-enabled > div > div")
    find7_loc = (By.XPATH, "//*[text()='排除']")
    #删除
    delete_loc=(By.CSS_SELECTOR,".pd3x.mg2t > div > div.fright > button:nth-child(2)")
    #删除确认
    deletesure_loc=(By.CSS_SELECTOR,".ant-popover-buttons > button.ant-btn.ant-btn-primary.ant-btn-sm > span")

    def type_traffic(self):
        self.find_element(*self.traffic_loc).click()

    def type_retention1(self):
        self.find_element(*self.retention1_loc).click()

    def type_addchoice(self):
        self.find_element(*self.addchoice_loc).click()

    def type_check(self):
        self.find_element(*self.check_loc).click()

    def type_input1(self):
        self.find_element(*self.input1_loc).click()

    def type_find1(self):
        self.find_element(*self.find1_loc).click()

    def type_time1(self):
        self.find_element(*self.time1_loc).click()

    # def type_time2(self):
    #     self.find_element(*self.time2_loc).click()
    #
    # def type_time3(self,time):
    #     self.find_element(*self.time3_loc).click()
    #     self.find_element(*self.time3_loc).clear()
    #     self.find_element(*self.time3_loc).send_keys(time)
    #     self.find_element(*self.timeallsureanalytic_loc).click()
    #
    # def type_time4(self):
    #     self.find_element(*self.time4_loc).click()
    #
    # def type_timesureanalytic(self):
    #     self.find_element(*self.timesureanalytic_loc).click()

    def type_input2(self):
        self.find_element(*self.input2_loc).click()

    def type_find2(self):
        self.find_element(*self.find2_loc).click()

    def type_input21(self):
        self.find_element(*self.input21_loc).click()


    def type_find3(self):
        self.find_element(*self.find3_loc).click()


    def type_surebutton(self):
        self.find_element(*self.surebutton_loc).click()

    def type_input3(self):
        self.find_element(*self.input3_loc).click()

    def type_find4(self):
        self.find_element(*self.find4_loc).click()

    def type_input31(self,value):
        self.find_element(*self.input31_loc).click()
        self.find_element(*self.input31_loc).send_keys(value)

    def type_input32(self,value):
        self.find_element(*self.input32_loc).click()
        self.find_element(*self.input32_loc).send_keys(value)

    def type_savebutton1(self):
        self.find_elevment(*self.savebutton1_loc).click()

    def type_inputname(self):
        self.find_element(*self.inputname_loc).click()

    def type_savebutton2(self):
        self.find_element(*self.savebutton2_loc).click()

    def type_maintime(self):
        self.find_element(*self.maintime_loc).click()

    def type_retention(self,*loc):
        for abc in self.driver.find_elements(*loc):
            if abc.is_displayed():
                abc.click()

    def type_retention_send(self,send_values,*loc):
        self.find_element(*loc).send_keys(send_values)



    def retention_action1(self,time1,time2):
        self.type_traffic()
        sleep(1)
        self.type_retention1()
        sleep(2)
        self.type_maintime()
        sleep(0.5)
        self.time_type(time1,time2)
        sleep(1)
        self.type_addchoice()
        sleep(0.5)
        self.type_input1()
        sleep(2)
        self.type_find1()
        self.type_time1()
        sleep(1)
        self.time_type(time1,time2)
        sleep(1)
        self.type_check()

    def retention_action2(self):
        self.type_retention(*self.retention2_loc)
        sleep(1)
        self.type_retention(*self.input4_loc)
        sleep(1.5)
        self.type_retention(*self.find5_loc)
        sleep(1)
        self.type_retention(*self.input5_loc)
        sleep(1.5)
        self.type_retention(*self.find51_loc)
        sleep(1)
        self.type_retention(*self.addchoice_loc)
        sleep(0.5)
        self.type_retention(*self.input2_loc)
        sleep(0.5)
        self.type_retention(*self.find2_loc)
        sleep(0.5)
        self.type_retention(*self.input21_loc)
        sleep(1)
        self.type_retention(*self.find3_loc)
        sleep(0.5)
        self.type_retention(*self.surebutton_loc)
        sleep(1)
        self.type_retention(*self.check_loc)

    def retention_action3(self):
        self.type_retention(*self.retention3_loc)
        sleep(0.5)
        self.type_retention(*self.input6_loc)
        sleep(0.5)
        self.type_retention(*self.find6_loc)
        sleep(1)
        self.type_retention(*self.addchoice_loc)
        sleep(0.5)
        self.type_retention(*self.input3_loc)
        sleep(0.5)
        self.type_retention(*self.find4_loc)
        sleep(1)
        self.type_retention(*self.input7_loc)
        sleep(0.5)
        self.type_retention(*self.find7_loc)
        sleep(1)
        self.type_retention(*self.input31_loc)
        sleep(0.5)
        self.type_retention_send('2',*self.input31_loc)
        sleep(0.5)
        self.type_retention(*self.input32_loc)
        sleep(0.5)
        self.type_retention_send('10',*self.input32_loc)
        sleep(1)
        self.type_retention(*self.check_loc)

    def retention_action4(self):
        self.type_retention(*self.savebutton1_loc)
        sleep(0.5)
        self.type_retention(*self.inputname_loc)
        self.type_retention_send('测试留存',*self.inputname_loc)
        sleep(0.5)
        self.type_retention(*self.savebutton2_loc)

    def retention_action5(self):
        self.type_retention(*self.delete_loc)
        sleep(0.5)
        self.type_retention(*self.deletesure_loc)

    assert1_loc=(By.CSS_SELECTOR,".ant-table-row.ant-table-row-level-0 > td.grid > div")
    def type_assert1(self):
        return self.find_element(*self.assert1_loc).text

    assert2_loc=(By.CSS_SELECTOR,".ant-message-custom-content.ant-message-success>span")
    def type_assert2(self):
        return self.find_element(*self.assert2_loc).text