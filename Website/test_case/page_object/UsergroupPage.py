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
    savebutton_loc=(By.CSS_SELECTOR,"#main-content > div > div > div.scroll-content-100.always-display-scrollbar > div > div > div > div.ug-info.overscoll-y.pd3b > div > form > div:nth-child(6) > div > div > button")
    #更新按钮
    update_loc=(By.CSS_SELECTOR,".ant-form-item-control> button:nth-child(3) > span")
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

    #新建分群
    def usergroup_action1(self):
        self.type_click(*self.traffic_loc)
        sleep(1)
        self.type_click(*self.usergroup_loc)
        sleep(1)
        self.type_click(*self.addgroup_loc)
        sleep(1)
        self.type_send("测试分群%s"%self.nowtime(),*self.groupname_loc)
        sleep(1)
        self.type_click(*self.time1_loc)
        sleep(1)
        self.time_type("2017-07-15 00:00:00","2017-07-18 00:00:00")
        sleep(1)
        self.type_click(*self.uesradd1_loc)
        sleep(1)
        self.type_click(*self.pagename1_loc)
        sleep(1)
        self.type_click(*self.find1_loc)
        sleep(1)
        self.type_send("10",*self.inputnumble1_loc)
        sleep(1)
        self.type_click1(*self.savebutton_loc)


    def usergroup_action2(self):
        self.type_click(*self.useradd2_loc)
        sleep(1)
        self.type_click(*self.pagename2_loc)
        sleep(2)
        self.type_click(*self.find2_loc)
        sleep(2)
        self.type_send("10",*self.inputnumble2_loc)
        sleep(1)
        self.type_click(*self.useradd3_loc)
        sleep(1)
        self.type_click(*self.pagename3_loc)
        sleep(1)
        self.type_click(*self.find3_loc)
        sleep(1)
        self.type_click(*self.inputnumble3_loc)
        sleep(1)
        self.type_click(*self.find4_loc)
        sleep(1)
        self.type_click(*self.update_loc)

    def usergroup_action3(self):
        self.type_click(*self.path_loc)

    def usergroup_action4(self):
        self.type_click(*self.retention_loc)

    def usergroup_action5(self):
        self.type_click(*self.funnel_loc)

    def usergroup_action6(self):
        self.type_click(*self.traffic_loc)
        sleep(1)
        self.type_click(*self.usergroup_loc)
        sleep(1)
        self.type_click(*self.action_loc)

    def usergroup_action7(self):
        self.type_click(*self.seeuser_loc)

    def usergroup_action8(self):
        self.type_click(*self.updateuser_loc)

    def usergroup_action9(self):
        self.type_click(*self.deleteuser_loc)
        sleep(1)
        self.type_click(*self.deletesuer_loc)



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
    updateuser1_loc=(By.CSS_SELECTOR,'#main-content > div > div > div.scroll-content-100.always-display-scrollbar > div > div > div > div.ug-info.overscoll-y.pd3b > div > div > div > div > button:nth-child(3)')

    def type_seeuser1(self):
        return self.find_element(*self.seeuser1_loc).text

    def type_updateuser1(self):
        return self.find_element(*self.updateuser1_loc).text

