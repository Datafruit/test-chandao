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

    #新建单图步骤
    def slices_action1(self,name):
        self.type_click(*self.overview_loc)
        sleep(1)
        self.type_click(*self.slices_loc)
        sleep(1)
        self.type_click(*self.newslices_loc)
        sleep(1)
        self.type_click(*self.addwslices_loc)
        sleep(1)
        self.type_click(*self.addchoiceslices_loc)
        sleep(1)
        self.type_click(*self.doslices_loc)
        sleep(1)
        self.type_click(*self.saveslices_loc)
        sleep(1)
        self.type_send(name,*self.nameslices_loc)
        sleep(1)
        self.type_click(*self.suresaveslices_loc)

    #分享单图
    def slices_action2(self):
        self.type_click(*self.overview_loc)
        sleep(1)
        self.type_click(*self.slices_loc)
        sleep(1)
        self.type_findslices()
        sleep(1)
        self.type_click(*self.shareslices_loc)
        sleep(1)
        self.type_click(*self.ghostslices_loc)
        sleep(1)
        self.type_click(*self.successslice_loc)

    #单图加入概览
    def slices_action3(self):
        self.type_findslices()
        sleep(1)
        self.type_click(*self.pushpinslices_loc)

    #单图订阅
    def slices_action4(self):
        self.type_findslices()
        sleep(1)
        self.type_click(*self.starslices_loc)

    #单图删除
    def slices_action5(self):
        self.type_findslices()
        sleep(1)
        self.type_click(*self.crossslices_loc)
        sleep(1)
        self.type_click(*self.surecrossslices_loc)







    titileslices_loc=(By.CSS_SELECTOR,".ant-message > span > div > div > div > span > div")

    def type_titileslices(self):
       return self.find_element(*self.titileslices_loc).text

    allslices_loc=(By.CSS_SELECTOR,".ant-message > span > div > div > div > span")

    def type_allslices(self):
        return self.find_element(*self.allslices_loc).text

    def type_falsefind(self):
        return self.find_element(*self.findslices_loc).text