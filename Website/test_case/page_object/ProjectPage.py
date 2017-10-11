from page_object.BasePage import *
from selenium.webdriver.common.action_chains import ActionChains
class ProjectPage(Page):
    #数据管理
    project_loc=(By.XPATH,'//*[text()="数据管理"]')
    #新建项目
    newproject_loc=(By.CSS_SELECTOR,"#main-content > div > div > div.scroll-content.always-display-scrollbar > div > div.pd2b.fix > div.fright > a > button > span")
    #输入项目名称
    input1_loc=(By.CSS_SELECTOR,".fix.mg-auto.mw550.mg3t.pd3t > div.fleft.width250 > input")
    #下一步
    next_loc=(By.CSS_SELECTOR,"#main-content > div > div > div.scroll-content.always-display-scrollbar > div > div > div:nth-child(4) > div:nth-child(2) > button")
    #上传文件
    update_loc=(By.CSS_SELECTOR,".ant-upload.ant-upload-select.ant-upload-select-text > span > button")
    #删除按钮
    delete_loc=(By.CSS_SELECTOR,"tr:nth-child(1) > td:nth-child(7) > div > i.sugoicon.sugo-trash.color-grey.font14.pointer.hover-color-red.mg1l")
    #删除确认
    deletesure_loc=(By.CSS_SELECTOR,".ant-popover-inner > div > div > div.ant-popover-buttons > button.ant-btn.ant-btn-primary.ant-btn-sm")
    #鼠标移动
    move_loc=(By.CSS_SELECTOR,".ant-table-wrapper > div > div > div > div > div > table > tbody > tr:nth-child(1) > td.alignleft")
    #修改/确认修改
    change_loc=(By.CSS_SELECTOR,"tr:nth-child(1) > td.alignleft > div > div > i")
    #输入框
    input2_loc=(By.CSS_SELECTOR,"tr:nth-child(1) > td.alignleft > div > div > input")
    #数据接入
    click1_loc=(By.CSS_SELECTOR,"tr:nth-child(1) > td:nth-child(6) > div > span:nth-child(1) > a")
    #维度管理
    click2_loc = (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(6) > div > span:nth-child(2) > a")
    #指标管理
    click3_loc = (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(6) > div > span:nth-child(3) > a")
    #场景数据设置
    click4_loc = (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(6) > div > span:nth-child(4) > a")
    #设置
    set_loc=(By.CSS_SELECTOR,"tr:nth-child(1) > td:nth-child(7) > div > i.sugoicon.sugo-security.color-grey.font14.pointer.hover-color-main")
    #第一个用户组
    frist_loc=(By.CSS_SELECTOR,".ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > button:nth-child(1)")
    #提交按钮
    setup_loc=(By.CSS_SELECTOR,".ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-success.mg1r.iblock")




    def project_action1(self):
        self.type_click(*self.project_loc)
        sleep(1)
        self.type_click(*self.newproject_loc)
        sleep(1)
        self.type_send("测试项目",*self.input1_loc)
        sleep(1)
        self.type_click(*self.next_loc)
        sleep(1)
        self.type_click(*self.project_loc)
        # self.driver.find_element(*self.update_loc).send_keys(r"E:\工作资料\ydxx_sample.csv")


    def project_action2(self):
        move=self.find_element(*self.move_loc)
        ActionChains(self.driver).move_to_element(move).perform()
        sleep(0.5)
        self.type_click(*self.change_loc)
        sleep(1)
        self.type_send("测试项目1",*self.input2_loc)
        sleep(1)
        self.type_click(*self.change_loc)

    def project_action3(self):
        self.type_click(*self.click1_loc)

    def project_action4(self):
        self.type_click(*self.click2_loc)

    def project_action5(self):
        self.type_click(*self.click3_loc)

    def project_action6(self):
        self.type_click(*self.click4_loc)

    def project_action7(self):
        self.type_click(*self.set_loc)
        sleep(0.5)
        self.type_click(*self.frist_loc)
        sleep(0.5)
        self.type_click(*self.setup_loc)

    def project_action8(self):
        self.type_click(*self.delete_loc)
        sleep(0.5)
        self.type_click(*self.deletesure_loc)




    assert1_loc=(By.CSS_SELECTOR,".ant-message-custom-content.ant-message-info>span")
    def type_assert1(self):
        return self.find_element(*self.assert1_loc).text

    assert2_loc=(By.CSS_SELECTOR,"tr:nth-child(1) > td.alignleft > div > div > span")
    def type_assert2(self):
        return self.find_element(*self.assert2_loc).text

    assert3_loc=(By.CSS_SELECTOR,".itblock > div:nth-child(1) > div > span:nth-child(1) > span.mw200.itblock.elli > a > b")
    def type_assert3(self):
        return self.find_element(*self.assert3_loc).text

    assert4_loc=(By.CSS_SELECTOR,"#main-content > div > div.nav-bar > div > div.itblock > div:nth-child(1) > div > span > span.mw200.itblock.elli > b")
    def type_assert4(self):
        return self.find_element(*self.assert4_loc).text
