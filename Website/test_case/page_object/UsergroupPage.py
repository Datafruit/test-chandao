from page_object.BasePage import *
from selenium.webdriver.common.by import By
from time import sleep

class UsergroupPage(Page):
    #用户运营
    traffic_loc=(By.XPATH,'//*[text()="用户运营"]')
    usergroup_loc=(By.XPATH,'//*[text()="用户分群"]')
    #新建按钮
    addgroup_loc=(By.CSS_SELECTOR,"#main-content > div > div > div.nav-bar > div > div.fright.line-height42 > a > button")
    #输入框
    groupname_loc=(By.CSS_SELECTOR,".ant-input.ant-input-lg")
    #时间框
    time1_loc=(By.CSS_SELECTOR,".ug-form-options > div:nth-child(1) > div.ant-col-18.ant-form-item-control-wrapper > div > div")
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
    #用户行为筛选
    uesradd1_loc=(By.CSS_SELECTOR,".ug-form-options > div:nth-child(2) > div.ant-col-18.ant-form-item-control-wrapper > div > div.add-button-wrap > span")
    #页面名称
    pagename1_loc=(By.CSS_SELECTOR,".sub-filters > div > div > div:nth-child(1) > div:nth-child(1) > div.width-100.ant-select.ant-select-enabled.ant-select-allow-clear > div > div")
    #查找手机平台首页
    find1_loc=(By.XPATH,"//*[text()='手机平台首页']")
    #输入数量
    inputnumble1_loc=(By.CSS_SELECTOR,".sub-filters > div > div > div:nth-child(3) > div > div.ant-input-number-input-wrap > input")
    #指标筛选
    useradd2_loc=(By.CSS_SELECTOR,".ug-form-options > div:nth-child(3) > div.ant-col-18.ant-form-item-control-wrapper > div > div.add-button-wrap > span")
    #选择指标筛选
    pagename2_loc=(By.CSS_SELECTOR,".sub-filters > div > div > div:nth-child(1) > div.width140.mg1r.inline.ant-select.ant-select-enabled > div > div")
    #查找总记录
    find2_loc=(By.XPATH,"//*[text()='总记录数']")
    #输入大于数值
    inputnumble2_loc=(By.CSS_SELECTOR,".ug-form-options > div:nth-child(3) > div.ant-col-18.ant-form-item-control-wrapper > div > div.filters > div > div > div.sub-filters > div > div > div:nth-child(3) > div > div.ant-input-number-input-wrap > input")
    #一个条件
    useradd3_loc=(By.CSS_SELECTOR,".ug-form-options > div:nth-child(4) > div.ant-col-18.ant-form-item-control-wrapper > div > div.add-button-wrap > span")
    #选择条件
    pagename3_loc=(By.CSS_SELECTOR,".sub-filters > div > div > div:nth-child(1) > div.width140.mg1r.iblock.ant-select.ant-select-enabled > div > div")
    #查找省份
    find3_loc=(By.XPATH,"//*[text()='省份']")
    #输入数量
    inputnumble3_loc=(By.CSS_SELECTOR,".sub-filters > div > div > div.iblock > div.inline.width140.mg1r.ant-select.ant-select-enabled > div > div")
    #查找广东省
    find4_loc = (By.XPATH, "//*[text()='广东省']")
    #保存按钮
    savebutton_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-success.ant-btn-lg")
    #更新按钮
    update_loc=(By.CSS_SELECTOR,".ant-form-item-control> button:nth-child(2) > span")
    #跳转路径分析
    path_loc=(By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/a[1]')
    #跳转留存分析
    retention_loc=(By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/a[2]')
    #跳转漏斗分析
    funnel_loc=(By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/a[3]')
    #跳转事件分析
    action_loc=(By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/a[4]')
    #查看用户跳转
    seeuser_loc=(By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/a[1]')
    #编辑跳转
    updateuser_loc=(By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/a[2]')
    #删除
    deleteuser_loc=(By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/span')
    #删除确定按钮
    deletesuer_loc=(By.CSS_SELECTOR,'.ant-btn.ant-btn-primary.ant-btn-sm')

    def type_traffic(self):
        self.find_element(*self.traffic_loc).click()

    def type_usergroup(self):
        self.find_element(*self.usergroup_loc).click()

    def type_addgroup(self):
        self.find_element(*self.addgroup_loc).click()

    def type_groupname(self,name):
        self.find_element(*self.groupname_loc).send_keys(name)

    def type_time1(self):
        self.find_element(*self.time1_loc).click()

    def type_time2(self):
        self.find_element(*self.time2_loc).click()

    def type_time3(self,time):
        self.find_element(*self.time3_loc).click()
        self.find_element(*self.time3_loc).clear()
        self.find_element(*self.time3_loc).send_keys(time)
        self.find_element(*self.timeallsureanalytic_loc).click()

    def type_time4(self):
        self.find_element(*self.time4_loc).click()

    def type_timesureanalytic(self):
        self.find_element(*self.timesureanalytic_loc).click()

    def type_uesradd1(self):
        self.find_element(*self.uesradd1_loc).click()

    def type_useradd2(self):
        self.find_element(*self.useradd2_loc).click()

    def type_useradd3(self):
        self.find_element(*self.useradd3_loc).click()

    def type_pagename1(self):
        self.find_element(*self.pagename1_loc).click()

    def type_pagename2(self):
        self.find_element(*self.pagename2_loc).click()

    def type_pagename3(self):
        self.find_element(*self.pagename3_loc).click()

    def type_find1(self):
        self.find_element(*self.find1_loc).click()

    def type_inputnumble1(self):
        self.find_element(*self.inputnumble1_loc).click()
        self.find_element(*self.inputnumble1_loc).send_keys("10")

    def type_find2(self):
        self.find_element(*self.find2_loc).click()

    def type_inputnumble2(self):
        self.find_element(*self.inputnumble2_loc).send_keys("20")

    def type_find3(self):
        self.find_element(*self.find3_loc).click()

    def type_inputnumble3(self):
        self.find_element(*self.inputnumble3_loc).click()

    def type_find4(self):
        self.find_element(*self.find4_loc).click()

    def type_savebutton(self):
        self.find_element(*self.savebutton_loc).click()

    def type_update(self):
        self.find_element(*self.update_loc).click()

    def type_choice1(self):
        self.find_element(*self.path_loc).click()

    def type_choice2(self):
        self.find_element(*self.retention_loc).click()

    def type_choice3(self):
        self.find_element(*self.funnel_loc).click()

    def type_choice4(self):
        self.find_element(*self.action_loc).click()

    def type_seeuser(self):
        self.find_element(*self.seeuser_loc).click()

    def type_updateuser_loc(self):
        self.find_element(*self.updateuser_loc).click()

    def type_deleteuser_loc(self):
        self.find_element(*self.deleteuser_loc).click()

    def type_deletesuer_loc(self):
        self.find_element(*self.deletesuer_loc).click()





    #新建分群
    def usergroup_action1(self,name,time1,time2):
        self.type_traffic()
        sleep(1)
        self.type_usergroup()
        sleep(2)
        self.type_addgroup()
        sleep(2)
        self.type_groupname(name)
        sleep(2)
        self.type_time1()
        sleep(1)
        self.type_time2()
        sleep(1)
        self.type_time3(time1)
        sleep(1)
        self.type_time4()
        sleep(1)
        self.type_time3(time2)
        sleep(1)
        self.type_timesureanalytic()
        sleep(1)
        self.type_uesradd1()
        sleep(0.5)
        self.type_pagename1()
        sleep(2)
        self.type_find1()
        sleep(1)
        self.type_inputnumble1()
        sleep(1)
        self.type_useradd2()
        sleep(0.5)
        self.type_pagename2()
        sleep(2)
        self.type_find2()
        sleep(1)
        self.type_inputnumble2()
        sleep(0.5)
        self.type_savebutton()

    def usergroup_action2(self):
        self.type_useradd3()
        sleep(0.5)
        self.type_pagename3()
        sleep(1)
        self.type_find3()
        sleep(1)
        self.type_inputnumble3()
        sleep(2)
        self.type_find4()
        sleep(0.5)
        self.type_update()

    def usergroup_action3(self):
        self.type_choice1()

    def usergroup_action4(self):
        self.type_choice2()

    def usergroup_action5(self):
        self.type_choice3()

    def usergroup_action6(self):
        self.type_traffic()
        sleep(1)
        self.type_usergroup()
        sleep(2)
        self.type_choice4()

    def usergroup_action7(self):
        self.type_seeuser()

    def usergroup_action8(self):
        self.type_updateuser_loc()

    def usergroup_action9(self):
        self.type_deleteuser_loc()
        sleep(1)
        self.type_deletesuer_loc()


    message_loc=(By.CSS_SELECTOR,".ant-message-custom-content.ant-message-success>span")

    def type_message(self):
            return self.find_element(*self.message_loc).text

    number_loc=(By.CSS_SELECTOR,".usergroup-list-wrapper > div:nth-child(1) > a > span")

    def type_number(self):
        return self.find_element(*self.number_loc).get_attribute("title")  #获取title属性中的值

    choice11_loc=(By.CSS_SELECTOR,".fright > span > button > span")
    choice21_loc = (By.CSS_SELECTOR, ".fright > button > span")
    choice31_loc = (By.CSS_SELECTOR, ".fright > button > span")
    choice41_loc = (By.CSS_SELECTOR, ".ant-row > div.ant-col-6 > div > div > button.ant-btn.ant-btn-success.mg1r > span")

    def type_choice11(self):
        return self.find_element(*self.choice11_loc).text

    def type_choice21(self):
        return self.find_element(*self.choice21_loc).text

    def type_choice31(self):
        return self.find_element(*self.choice31_loc).text

    def type_choice41(self):
        return self.find_element(*self.choice41_loc).text

    seeuser1_loc=(By.CSS_SELECTOR,"#main-content > div > div.nav-bar > div > div.itblock > div:nth-child(1) > div > span > span.mw200.itblock.elli > a > b")
    updateuser1_loc=(By.CSS_SELECTOR,'.ug-info > div > div > div > div > button:nth-child(2) > span')

    def type_seeuser1(self):
        return self.find_element(*self.seeuser1_loc).text

    def type_updateuser1(self):
        return self.find_element(*self.updateuser1_loc).text

