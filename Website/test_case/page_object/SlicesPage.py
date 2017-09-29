from time import sleep
from page_object.BasePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SlicesPage(Page):
    #定位器
    #图表
    overview_loc=(By.XPATH,".//*[@id='main-header']/span[1]/span/a[1]")
    #单图
    slices_loc=(By.XPATH,'//*[@id="container"]/div/div[2]/div[2]/a[3]')
    #查找单图
    findslices_loc=(By.LINK_TEXT,"测试单图")
    #分享
    shareslices_loc=(By.CSS_SELECTOR,".anticon.anticon-share-alt.pointer.mg1r")
    #选择分享组
    ghostslices_loc=(By.CSS_SELECTOR,".ant-modal-body > button:nth-child(2)")
    #提交确定按钮
    successslice_loc=(By.CSS_SELECTOR,".ant-modal-body > div > button")
    #加入概览
    pushpinslices_loc=(By.CSS_SELECTOR,".anticon.anticon-pushpin-o.pointer.mg1r")
    #订阅
    starslices_loc=(By.CSS_SELECTOR,".anticon.anticon-star-o.pointer.mg1r")
    #删除
    crossslices_loc=(By.CSS_SELECTOR,".slice-head > div.fix.font14 > div > i.anticon.anticon-cross-circle-o.pointer.color-red")
    #删除确定
    surecrossslices_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.ant-btn-sm")
    #新建单图
    newslices_loc=(By.CSS_SELECTOR,".fright.line-height42 > a > button")
    #添加维度
    addwslices_loc=(By.XPATH,"//*[text()='页面名称']")
    addchoiceslices_loc=(By.CSS_SELECTOR,".ant-popover-inner > div > div > div > button:nth-child(2)")
    #执行查询
    doslices_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-success.font14.center-of-relative")
    #点击保存按钮
    saveslices_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-success")
    #输入名称
    nameslices_loc=(By.CSS_SELECTOR,".ant-input.width-100")
    #确认保存
    suresaveslices_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-primary.width-100")

    def type_overview(self):
        self.find_element(*self.overview_loc).click()

    def type_slices(self):
        self.find_element(*self.slices_loc).click()
    def type_findslices(self):
        findadress=self.find_element(*self.findslices_loc)
        ActionChains(self.driver).move_to_element(findadress).perform()

    def type_shareslices(self):
        self.find_element(*self.shareslices_loc).click()

    def type_ghostslices(self):
        self.find_element(*self.ghostslices_loc).click()

    def type_successslice(self):
        self.find_element(*self.successslice_loc).click()

    def type_pushpinslices(self):
        self.find_element(*self.pushpinslices_loc).click()

    def type_starslices(self):
        self.find_element(*self.starslices_loc).click()

    def type_crossslices(self):
        self.find_element(*self.crossslices_loc).click()

    def type_surecrossslices(self):
        self.find_element(*self.surecrossslices_loc).click()

    def type_newslices(self):
        self.find_element(*self.newslices_loc).click()

    def type_addwslices(self):
        self.find_element(*self.addwslices_loc).click()

    def type_addchoiceslices(self):
        self.find_element(*self.addchoiceslices_loc).click()

    def type_doslices(self):
        self.find_element(*self.doslices_loc).click()

    def type_saveslices(self):
        self.find_element(*self.saveslices_loc).click()

    def type_nameslices(self,name):
        # self.find_element(*self.nameslices_loc).clear()
        self.find_element(*self.nameslices_loc).send_keys(name)

    def type_suresaveslices(self):
        self.find_element(*self.suresaveslices_loc).click()

    #新建单图步骤
    def slices_action1(self,name):
        self.type_overview()
        sleep(2)
        self.type_slices()
        sleep(2)
        self.type_newslices()
        sleep(3)
        self.type_addwslices()
        self.type_addchoiceslices()
        sleep(1)
        self.type_doslices()
        sleep(2)
        self.type_saveslices()
        sleep(1)
        self.type_nameslices(name)
        sleep(1)
        self.type_suresaveslices()

    #分享单图
    def slices_action2(self):
        self.type_overview()
        sleep(2)
        self.type_slices()
        sleep(2)
        self.type_findslices()
        sleep(1)
        self.type_shareslices()
        sleep(1)
        self.type_ghostslices()
        sleep(1)
        self.type_successslice()

    #单图加入概览
    def slices_action3(self):
        # self.type_overview()
        # sleep(2)
        # self.type_slices()
        # sleep(2)
        self.type_findslices()
        sleep(1)
        self.type_pushpinslices()

    #单图订阅
    def slices_action4(self):
        # self.type_overview()
        # sleep(2)
        # self.type_slices()
        # sleep(2)
        self.type_findslices()
        sleep(1)
        self.type_starslices()

    #单图删除
    def slices_action5(self):
        # self.type_overview()
        # sleep(2)
        # self.type_slices()
        # sleep(2)
        self.type_findslices()
        sleep(1)
        self.type_crossslices()
        sleep(1)
        self.type_surecrossslices()







    titileslices_loc=(By.CSS_SELECTOR,".ant-message > span > div > div > div > span > div")

    def type_titileslices(self):
       return self.find_element(*self.titileslices_loc).text

    allslices_loc=(By.CSS_SELECTOR,".ant-message > span > div > div > div > span")

    def type_allslices(self):
        return self.find_element(*self.allslices_loc).text

    def type_falsefind(self):
        return self.find_element(*self.findslices_loc).text