from  page_object.BasePage import *

class UseractionPage(Page):
    #用户运营
    traffic_loc=(By.XPATH,'//*[text()="用户运营"]')
    useraction_loc=(By.XPATH,'//*[text()="事件分析"]')
    #页面名称
    page_loc=(By.CSS_SELECTOR,"div:nth-child(1) > div.width-100.ant-select.ant-select-enabled > div")
    page1_loc = (By.XPATH, '//*[text()="手机平台首页"]')
    #事件名称
    event_loc=(By.CSS_SELECTOR,"div:nth-child(2) > div.width-100.ant-select.ant-select-enabled > div")
    event1_loc = (By.XPATH, '//*[text()="华为品牌列表页"]')
    #事件类型
    type_loc=(By.CSS_SELECTOR,"div:nth-child(3) > div.width-100.ant-select.ant-select-enabled > div")
    type1_loc=(By.XPATH, '//*[text()="点击"]')
    #总次数
    all_loc=(By.CSS_SELECTOR,"div:nth-child(4) > div > div")
    all1_loc=(By.XPATH, '//*[text()="总人数"]')
    all2_loc = (By.XPATH, '//*[text()="平均次数"]')
    all3_loc = (By.XPATH, '//*[text()="人均次数"]')
    all4_loc = (By.XPATH, '//*[text()="总时长"]')
    all5_loc= (By.XPATH, '//*[text()="平均浏览时长"]')
    all6_loc = (By.XPATH, '//*[text()="人均浏览时长"]')
    all7_loc = (By.XPATH, '//*[text()="总次数"]')
    #时间框
    time_loc=(By.CSS_SELECTOR,"#main-content > div > div.scroll-content.always-display-scrollbar > div.pd2y.pd3x.bg-grey-f7 > div > div.mg0.bordert.dashed > div > div.ant-col-18 > div > div > div.mg2b.height32 > div")
    #添加一个条件
    addnew_loc=(By.CSS_SELECTOR,".ant-col-18 > div > div > div.pd1t > span")
    find1_loc=(By.CSS_SELECTOR,".ant-select-lg.width120.inline.mg1r.ant-select.ant-select-enabled > div > div")
    choice1_loc=(By.XPATH,'//li[text()="客户端事件时间"]')
    find2_loc=(By.CSS_SELECTOR,".mg1b > div > div.time-picker-format.relative.iblock.width200.height32.itblock.line-height18")
    #查询按钮
    query_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.width100")
    #保存按钮
    savebutton1_loc=(By.CSS_SELECTOR,".ant-col-6 > div > div > button.ant-btn.ant-btn-success.mg1r")
    #输入框
    input_loc=(By.CSS_SELECTOR,".ant-input.width-100")
    #确认保存按钮
    savebutton2_loc = (By.CSS_SELECTOR, ".ant-btn.ant-btn-primary.width-100")
    #删除按钮
    delect_loc=(By.CSS_SELECTOR,"#main-content > div > div.scroll-content.always-display-scrollbar > div.pd2y.pd3x.bg-grey-f7 > div > div.ant-row > div.ant-col-6 > div > div > button:nth-child(2)")
    #删除确认按钮
    delectsure_loc=(By.CSS_SELECTOR,".ant-popover-buttons > button.ant-btn.ant-btn-primary.ant-btn-sm > span")
    #选择分组
    choice_loc=(By.CSS_SELECTOR,".pd2y.pd3x.bg-grey-f7 > div > div:nth-child(3) > div > div > div")
    choice2_loc = (By.XPATH, '//*[text()="页面名称"]')
    #饼图
    image1_loc=(By.CSS_SELECTOR,".bordert.report-content > div:nth-child(2) > i")
    #一维柱图
    image2_loc = (By.CSS_SELECTOR, ".bordert.report-content > div:nth-child(3) > i")
    #一维面积图
    image3_loc = (By.CSS_SELECTOR, ".bordert.report-content > div:nth-child(4) > i")


    def useraction_action1(self):
        self.type_click(*self.traffic_loc)
        sleep(1)
        self.type_click(*self.useraction_loc)
        sleep(1)
        self.type_click(*self.page_loc)
        sleep(1)
        self.type_click(*self.page1_loc)
        sleep(1)
        self.type_click(*self.time_loc)
        sleep(1)
        self.time_type("2017-07-10 00:00:00","2017-07-19 00:00:00")
        sleep(1)
        self.type_click(*self.addnew_loc)
        sleep(1)
        self.type_click(*self.find1_loc)
        sleep(1)
        self.type_click(*self.choice1_loc)
        sleep(1)
        self.type_click(*self.find2_loc)
        sleep(1)
        self.time_type("2017-07-10 00:00:00", "2017-07-19 00:00:00")
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action2(self):
        self.type_click(*self.all_loc)
        sleep(1)
        self.type_click(*self.all1_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action3(self):
        self.type_click(*self.all_loc)
        sleep(1)
        self.type_click(*self.all2_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action4(self):
        self.type_click(*self.all_loc)
        sleep(1)
        self.type_click(*self.all3_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action5(self):
        self.type_click(*self.all_loc)
        sleep(1)
        self.type_click(*self.all4_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action6(self):
        self.type_click(*self.all_loc)
        sleep(1)
        self.type_click(*self.all5_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action7(self):
        self.type_click(*self.all_loc)
        sleep(1)
        self.type_click(*self.all6_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action8(self):
        self.type_click(*self.all_loc)
        sleep(1)
        self.type_click(*self.all7_loc)
        sleep(1)
        self.type_click(*self.event_loc)
        sleep(1)
        self.type_click1(*self.event1_loc)
        sleep(1)
        self.type_click(*self.type_loc)
        sleep(1)
        self.type_click(*self.type1_loc)
        sleep(1)
        self.type_click(*self.choice_loc)
        sleep(1)
        self.type_click1(*self.choice2_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action9(self):
        self.type_click(*self.image1_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action10(self):
        self.type_click(*self.image2_loc)
        sleep(1)
        self.type_click(*self.query_loc)

    def useraction_action11(self):
        self.type_click(*self.image3_loc)
        sleep(1)
        self.type_click(*self.query_loc)


    def useraction_action12(self):
        self.type_click(*self.savebutton1_loc)
        sleep(1)
        self.type_send("测试事件",*self.input_loc)
        sleep(1)
        self.type_click(*self.savebutton2_loc)


    def useraction_action13(self):
        self.type_click(*self.delect_loc)
        sleep(1)
        self.type_click(*self.delectsure_loc)


    assert1_loc=(By.CSS_SELECTOR,".elli.itblock")
    def type_assert1(self):
        return self.find_element(*self.assert1_loc).get_attribute("title")

    assert2_loc=(By.CSS_SELECTOR,".ant-table-body > table > tbody > tr:nth-child(1) > td:nth-child(2) > span")
    def type_assert2(self):
        return self.find_element(*self.assert2_loc).get_attribute("title")

    assert3_loc=(By.CSS_SELECTOR,".ant-message-custom-content.ant-message-success>span")
    def type_assert3(self):
        return self.find_element(*self.assert3_loc).text