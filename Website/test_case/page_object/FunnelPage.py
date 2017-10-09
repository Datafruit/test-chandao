#coding:utf-8

from selenium.webdriver.common.by import By
from time import sleep
from page_object.BasePage import Page
from selenium.webdriver.common.action_chains import ActionChains

class FunnelPage(Page):
    #用户运营
    traffic_loc=(By.XPATH,'//*[text()="用户运营"]')
    funnel_loc=(By.XPATH,'//*[text()="漏斗分析"]')
    #创建新漏斗
    newfunnel_loc=(By.CSS_SELECTOR,"#main-content > div > div.pd2x.pd2t > button.ant-btn.ant-btn-primary.mg2l.width100")
    #添加漏斗层级
    addfunnel_loc=(By.CSS_SELECTOR,"#main-content > div > div.pd3x.comparableFunnelPanel > div > div > div.mg2t > button")
    #第一栏的事件类型
    type1_loc=(By.CSS_SELECTOR,"#main-content > div > div.pd3x.comparableFunnelPanel > div > div > div:nth-child(2) > div.funnel-bubble-box.editing.animate.shadowb-eee.until-hover > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(3) > div > div.width-100.ant-select.ant-select-enabled > div > div")
    #页面名称
    page_loc=(By.CSS_SELECTOR,"#main-content > div > div.pd3x.comparableFunnelPanel > div > div > div.funnelLayerEditor.last > div > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(1) > div > div.width-100.ant-select.ant-select-enabled > div > div")
    #事件名称
    event_loc=(By.CSS_SELECTOR,"#main-content > div > div.pd3x.comparableFunnelPanel > div > div > div.funnelLayerEditor.last > div > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(2) > div > div.width-100.ant-select.ant-select-enabled > div > div")
    #事件类型
    type_loc=(By.CSS_SELECTOR,"#main-content > div > div.pd3x.comparableFunnelPanel > div > div > div.funnelLayerEditor.last > div > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(3) > div > div.width-100.ant-select.ant-select-enabled > div > div")
    #获取浏览
    see1_loc=(By.XPATH,"//*[text()='浏览']")
    see2_loc = (By.XPATH, "//*[text()='中兴品牌列表页']")
    see3_loc = (By.XPATH, "//*[text()='手机平台首页']")
    see4_loc = (By.XPATH, "//*[text()='华为品牌列表页']")
    see5_loc = (By.XPATH, "//*[text()='筛选荣耀V9']")
    see6_loc = (By.XPATH, "//*[text()='Apple品牌列表页']")
    see7_loc = (By.XPATH, "//*[text()='停留']")
    see8_loc=(By.XPATH,"//*[text()='3 天']")
    see9_loc=(By.XPATH,"//*[text()='测试漏斗1']")
    #时间控件定位
    time_loc=(By.CSS_SELECTOR,"#main-content > div > div:nth-child(5) > div:nth-child(1) > div.mg2b.height32.line-height32 > div.time-picker-format.relative.iblock.iblock.width260.mg2r")
    #完成创建
    done_loc=(By.CSS_SELECTOR,"#main-content > div > button")
    #周期
    week_loc=(By.CSS_SELECTOR,".mg2b.height32.line-height32 > div.itblock.mg2r > div.iblock.mg1r.width60 > div > div > div")
    #编辑按钮
    changebutton_loc=(By.CSS_SELECTOR,"#main-content > div > div.pd2x.pd2t > button.ant-btn.mg1l.width100")
    #增加一个条件
    condition_loc=(By.CSS_SELECTOR,"#main-content > div > div:nth-child(5) > div:nth-child(1) > div.pd1t > span")
    #保存常用漏斗按钮
    savebutton1_loc=(By.CSS_SELECTOR,"#main-content > div > div:nth-child(2) > div.fright > button.ant-btn.ant-btn-success")
    #输入名称
    inputname_loc=(By.CSS_SELECTOR,".ant-tabs-tabpane.ant-tabs-tabpane-active > div > div:nth-child(2) > input")
    #保存
    savebutton2_loc=(By.CSS_SELECTOR,"#main-content > div > div:nth-child(2) > div.fright > button.ant-btn.ant-btn-success")
    #更新按钮
    updatebutton_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.width-100")
    #流失分析按钮
    lostbutton_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-ghost")
    #跳转到用户细查
    jump_loc=(By.CSS_SELECTOR,".ant-table-wrapper > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > a")
    #删除按钮
    deletebutton_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-default.mg1l")
    #删除确认
    deletesurebutton_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.ant-btn-sm")
    #下拉框
    drop_loc=(By.CSS_SELECTOR,"#main-content > div > div:nth-child(2) > div.itblock > div > div > div")


    def type_funnel_click(self,*loc):
        for abc in self.driver.find_elements(*loc):
            if abc.is_displayed():
                abc.click()

    def type_retention_send(self,send_values,*loc):
        for abc in self.driver.find_elements(*loc):
            if abc.is_displayed():
                abc.clear()
                abc.send_keys(send_values)


    def funnel_action1(self):
        self.type_funnel_click(*self.traffic_loc)
        sleep(1)
        self.type_funnel_click(*self.funnel_loc)
        sleep(1)
        # self.type_funnel_click(*self.newfunnel_loc)
        # sleep(1)
        # self.type_funnel_click(*self.type1_loc)
        # sleep(1)
        # self.type_funnel_click(*self.see1_loc)
        # sleep(1)
        # self.type_funnel_click(*self.page_loc)
        # sleep(1)
        # self.type_funnel_click(*self.see2_loc)
        # sleep(1)
        # self.type_funnel_click(*self.addfunnel_loc)
        # sleep(1)
        # self.type_funnel_click(*self.page_loc)
        # sleep(1)
        # self.type_funnel_click(*self.see3_loc)
        # sleep(1)
        # self.type_funnel_click(*self.type_loc)
        # sleep(1)
        # self.type_funnel_click(*self.see7_loc)
        # sleep(1)
        # self.type_funnel_click(*self.addfunnel_loc)
        # sleep(1)
        # self.type_funnel_click(*self.page_loc)
        # sleep(1)
        # self.type_funnel_click(*self.see4_loc)
        # sleep(1)
        # self.type_funnel_click(*self.event_loc)
        # sleep(1)
        # self.type_funnel_click(*self.see5_loc)
        # sleep(2)
        # self.type_funnel_click(*self.time_loc)
        # sleep(1)
        # self.time_type('2017-07-01 00:02:00','2017-07-31 00:05:00')
        # sleep(1)
        # self.type_funnel_click(*self.week_loc)
        # sleep(1)
        # self.type_funnel_click(*self.see8_loc)
        # sleep(1)
        # self.type_funnel_click(*self.done_loc)
    #
    # def funnel_action2(self):
    #     funnel=self.find_element(*self.savebutton1_loc)
    #     btn = self.driver.find_element_by_css_selector("#main-content > div > div:nth-child(2) > div.fright > button")
    #     act = ActionChains(self.driver).move_to_element(btn)
    #     sleep(1)
    #     act.perform()
        # self.driver.find_element(*self.savebutton1_loc).click()
        # self.type_funnel_click(*self.savebutton1_loc)
        # sleep(1)
        # self.driver.find_element(*self.inputname_loc).click()
        # # self.type_funnel_click(*self.inputname_loc)
        # sleep(1)
        # self.type_retention_send("测试漏斗",*self.inputname_loc)
        # sleep(1)
        # self.type_funnel_click(*self.savebutton2_loc)


    # def funnel_action3(self):
    #     self.type_funnel_click(*self.changebutton_loc)
    #     sleep(1)
    #     self.type_funnel_click(*self.addfunnel_loc)
    #     sleep(1)
    #     self.type_funnel_click(*self.page_loc)
    #     sleep(1)
    #     self.type_funnel_click(*self.see6_loc)
    #     sleep(1)
    #     self.type_funnel_click(*self.type_loc)
    #     sleep(1)
    #     self.type_funnel_click(*self.done_loc)
        sleep(1)
        # self.driver.find_element(*self.savebutton2_loc)
        self.type_funnel_click(*self.savebutton2_loc)

        sleep(2)
        self.driver.find_element(*self.inputname_loc)
        sleep(1)
        self.type_retention_send("测试漏斗1",*self.inputname_loc)
        sleep(1)
        self.type_funnel_click(*self.updatebutton_loc)

    def funnel_action4(self):
        self.type_funnel_click(*self.lostbutton_loc)
        sleep(1)
        self.type_funnel_click(*self.jump_loc)

    def funnel_action5(self):
        self.type_funnel_click(*self.drop_loc)
        sleep(1)
        self.type_funnel_click(*self.see9_loc)
        sleep(1)
        self.type_funnel_click(*self.deletebutton_loc)
        sleep(1)
        self.type_funnel_click(*self.deletesurebutton_loc)



    assert1_loc=(By.CSS_SELECTOR,".ant-message-custom-content.ant-message-success>span")
    def type_assert1(self):
        return self.find_element(*self.assert1_loc).text

    assert2_loc=(By.CSS_SELECTOR,"#main-content > div > div.nav-bar > div > div.itblock > div:nth-child(1) > div > span > span.mw200.itblock.elli > a > b")
    def type_assert2(self):
        return self.find_element(*self.assert2_loc).text

    assert3_loc=(By.CSS_SELECTOR,".ant-col-8.aligncenter > div:nth-child(2) > div.funnel-bubble-box.relative.bg-white > div:nth-child(2) > div > span")
    def type_assert3(self):
        return self.find_element(*self.assert3_loc).text