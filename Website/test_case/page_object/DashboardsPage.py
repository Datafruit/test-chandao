from page_object.BasePage import *

class DashboardsPage(Page):
    #图表
    overview_loc=(By.XPATH,"//*[text()='图表']")
    #数据看板
    dashboards_loc=(By.XPATH,"//*[text()='数据看板']")
    #新建看板
    newdashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/a/button")
    #看板名称
    newdashboardsname_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/input")
    #添加第一张单图
    add1dashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[1]/div[4]/div[1]/h3/span[2]/i")
    #添加第二个单图
    add2dashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[1]/div[4]/div[2]/h3/span[2]/i")
    #保存看板
    savedashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/button")
    #编辑看板
    changedashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/button[1]")
    #删除看板
    delete1dashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/button[2]")
    #删除弹窗确定按钮
    delete1agreedashboards_loc=(By.CSS_SELECTOR,"div.ant-popover-buttons > button.ant-btn.ant-btn-primary.ant-btn-sm > span")
    #更新看板
    updatedashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/button[1]")
    #退出编辑
    outdashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/button[2]")
    #编辑看板里面的删除
    delete2dashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div/button[3]")
    #订阅按钮
    spandashboards_loc=(By.CSS_SELECTOR,"div.slices-body > div.nav-bar > div > div.fleft > button.ant-btn.ant-btn-ghost.ant-btn-icon-only.mg1x.iblock")
    #分享按钮
    sharedashboards_loc=(By.CSS_SELECTOR,"#main-content > div > div > div > div > div > div > div.slices-body > div.nav-bar > div > div.fleft > button.ant-btn.ant-btn-ghost.ant-btn-icon-only.mg1l.iblock")
    #选择分享用户组
    sharechangedashboards_loc=(By.CSS_SELECTOR,"div.ant-modal-content > div.ant-modal-body > button:nth-child(2)")
    #提交分享设置按钮
    sharebuttondashboards_loc=(By.CSS_SELECTOR,"div.ant-modal-content > div.ant-modal-body > div > button")

#新增看板
    def dashboards_action1(self):
        self.type_click(*self.overview_loc)
        sleep(1)
        self.type_click(*self.dashboards_loc)
        sleep(1)
        self.type_click(*self.newdashboards_loc)
        sleep(1)
        self.type_send("数据看板%s"%self.nowtime(),*self.newdashboardsname_loc)
        sleep(1)
        self.type_click(*self.add1dashboards_loc)
        sleep(1)
        self.type_click(*self.savedashboards_loc)

#修改看板
    def dashboards_action2(self):
        self.type_click(*self.changedashboards_loc)
        sleep(1)
        self.type_click(*self.add2dashboards_loc)
        sleep(1)
        self.type_click(*self.updatedashboards_loc)

#分享看板
    def dashboards_action3(self):
        self.type_click(*self.sharedashboards_loc)
        sleep(1)
        self.type_click(*self.sharechangedashboards_loc)
        sleep(1)
        self.type_click(*self.sharebuttondashboards_loc)

#订阅看板
    def dashboards_action4(self):
        self.type_click(*self.spandashboards_loc)

#删除看板
    def dashboards_action5(self):
        self.type_click(*self.delete1dashboards_loc)
        sleep(1)
        self.type_click(*self.delete1agreedashboards_loc)

#看板不加单图
    def dashboards_action6(self):
        self.type_click(*self.newdashboards_loc)
        sleep(1)
        self.type_send("",*self.newdashboardsname_loc)
        sleep(1)
        self.type_click(*self.savedashboards_loc)



    dashboardsPass_loc=(By.CSS_SELECTOR,".ant-message-custom-content.ant-message-success>span")

    def dashboards_pass(self):
        return self.find_element(*self.dashboardsPass_loc).text

    def dashboards_error(self):
        return self.find_element(*self.savedashboards_loc).text
