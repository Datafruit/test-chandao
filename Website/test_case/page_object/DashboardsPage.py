from page_object.BasePage import *

class DashboardsPage(Page):
    #定位器
    #图表
    overview_loc=(By.XPATH,".//*[@id='main-header']/span[1]/span/a[1]")
    #数据看板
    dashboards_loc=(By.XPATH,".//*[@id='container']/div/div[2]/div[2]/a[4]")
    #新建看板
    newdashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/a/button")
    #看板名称
    newdashboardsname_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/input")
    #添加第一张单图
    add1dashboards_loc=(By.XPATH,".//*[@id='main-content']/div/div/div/div/div/div/div[1]/div[4]/div[1]/h3/span[2]/i")
    #查找名为数据看板的看板
    find_dashboards_loc=(By.LINK_TEXT,"测试看板")
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


    def type_overview(self):
        self.find_element(*self.overview_loc).click()

    def type_dashboards(self):
        self.find_element(*self.dashboards_loc).click()

    def type_newdashboards(self):
        self.find_element(*self.newdashboards_loc).click()

    def type_newdashboardsname(self,name):
        self.find_element(*self.newdashboardsname_loc).clear()
        self.find_element(*self.newdashboardsname_loc).send_keys(name)

    def type_find_dashboards(self):
        self.find_element(*self.find_dashboards_loc).click()

    def type_add1dashboards(self):
        self.find_element(*self.add1dashboards_loc).click()

    def type_add2dashboards(self):
        self.find_element(*self.add2dashboards_loc).click()

    def type_savedashboards(self):
        self.find_element(*self.savedashboards_loc).click()

    def type_changedashboards(self):
        self.find_element(*self.changedashboards_loc).click()

    def type_delete1dashboards(self):
        self.find_element(*self.delete1dashboards_loc).click()

    def type_delete1agreedashboards(self):
        self.find_element(*self.delete1agreedashboards_loc).click()

    def type_delete21dashboards(self):
        self.find_element(*self.delete2dashboards_loc).click()

    def type_updatedashboards(self):
        self.find_element(*self.updatedashboards_loc).click()

    def type_outdashboards(self):
        self.find_element(*self.outdashboards_loc).click()

    def type_spandashboards(self):
        self.find_element(*self.spandashboards_loc).click()

    def type_sharedashboards(self):
        self.find_element(*self.sharedashboards_loc).click()

    def type_sharechangedashboards(self):
        self.find_element(*self.sharechangedashboards_loc).click()

    def type_sharebuttondashboards(self):
        self.find_element(*self.sharebuttondashboards_loc).click()
#新增看板
    def dashboards_action1(self,name):
        self.type_overview()
        self.type_dashboards()
        sleep(2)
        self.type_newdashboards()
        sleep(2)
        self.type_newdashboardsname(name)
        sleep(2)
        self.type_add1dashboards()
        sleep(2)
        self.type_savedashboards()
#修改看板
    def dashboards_action2(self):
        # self.type_overview()
        # self.type_dashboards()
        # sleep(2)
        # self.type_find_dashboards()
        # sleep(2)
        self.type_changedashboards()
        self.type_add2dashboards()
        sleep(1)
        self.type_updatedashboards()
#分享看板
    def dashboards_action3(self):
        # self.type_overview()
        # self.type_dashboards()
        # sleep(2)
        # self.type_find_dashboards()
        # sleep(2)
        self.type_sharedashboards()
        sleep(1)
        self.type_sharechangedashboards()
        sleep(1)
        self.type_sharebuttondashboards()
#订阅看板
    def dashboards_action4(self):
        # self.type_overview()
        # self.type_dashboards()
        # sleep(2)
        # self.type_find_dashboards()
        # sleep(2)
        self.type_spandashboards()
#删除看板
    def dashboards_action5(self):
        # self.type_overview()
        # self.type_dashboards()
        # sleep(2)
        # self.type_find_dashboards()
        # sleep(2)
        self.type_delete1dashboards()
        sleep(1)
        self.type_delete1agreedashboards()
#看板不加单图
    def dashboards_action6(self,name):
        # self.type_overview()
        # self.type_dashboards()
        # sleep(2)
        self.type_newdashboards()
        sleep(2)
        self.type_newdashboardsname(name)
        sleep(2)
        self.type_savedashboards()


    dashboardsPass_loc=(By.CSS_SELECTOR,".ant-message-custom-content.ant-message-success>span")

    def dashboards_pass(self):
        return self.find_element(*self.dashboardsPass_loc).text

    def dashboards_error(self):
        return self.find_element(*self.savedashboards_loc).text


