from page_object.BasePage import *

class DimensionPage(Page):
    #数据管理
    project_loc=(By.XPATH,'//*[text()="数据管理"]')
    #维度管理
    dimension_loc=(By.XPATH,'//*[text()="维度管理"]')
    #新建维度
    add_loc=(By.CSS_SELECTOR,".pd2b > div > div.fright > button:nth-child(1)")
    #名称
    name1_loc=(By.CSS_SELECTOR,"#name")
    #别名
    name2_loc=(By.CSS_SELECTOR,"#title")
    #提交按钮
    set_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-success.mg1r.iblock")
    #维度应用
    choice1_loc=(By.CSS_SELECTOR,".width140.iblock.ant-select.ant-select-enabled > div > div")
    #已应用维度
    choice2_loc = (By.XPATH, '//li[text()="已应用维度"]')
    #未应用维度
    choice3_loc = (By.XPATH, '//li[text()="未应用维度"]')
    #排序和隐藏按钮
    upload_loc=(By.CSS_SELECTOR,".pd2b > div > div.fleft > button")
    #授权按钮
    authorization1_loc=(By.CSS_SELECTOR,".pd2b > div > div.fright > button.ant-btn.ant-btn-ghost.iblock.mg1l.ant-dropdown-trigger")
    #全部授权
    authorization2_loc = (By.XPATH, '//li[text()="全部授权"]')
    #授权组
    share_loc=(By.CSS_SELECTOR,".ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > button:nth-child(1)")
    #授权确认提交
    sharesure_loc=(By.CSS_SELECTOR,".ant-btn.ant-btn-success.iblock")
    #全部取消授权
    authorization3_loc = (By.XPATH, '//li[text()="全部取消授权"]')
    #标签按钮
    label1_loc=(By.CSS_SELECTOR,".pd2b > div > div.fright > div > button")
    #标签管理按钮
    label2_loc=(By.CSS_SELECTOR,".ant-popover-title > div > span.fright > button")
    #标签名称
    input_loc=(By.CSS_SELECTOR,".ant-modal-body > div.tag-create.pd2b > input")
    #新增标签
    addlabel_loc=(By.CSS_SELECTOR,".ant-modal-body > div.tag-create.pd2b > button")
    #标签删除
    deletelabel_loc=(By.CSS_SELECTOR," div:nth-child(1) > div > div > span.fright > i.anticon.anticon-close-circle-o.pointer.mg2x.font16.color-grey")
    #删除确认
    deletesure_loc=(By.CSS_SELECTOR,".ant-popover-buttons > button.ant-btn.ant-btn-primary.ant-btn-sm")
    #修改
    change_loc=(By.CSS_SELECTOR,"tr:nth-child(1) > td:nth-child(7) > div > i.sugoicon.sugo-edit.color-grey.font14.pointer.hover-color-main")
    #删除
    delete_loc=(By.CSS_SELECTOR,"tr:nth-child(1) > td:nth-child(7) > div > i.sugoicon.sugo-trash.mg2l.font14.color-grey.pointer.hover-color-red")



    def dimension_action1(self):
        self.type_click(*self.project_loc)
        sleep(1)
        self.type_click(*self.dimension_loc)
        sleep(1)
        self.type_click(*self.add_loc)
        sleep(0.5)
        self.type_send("aaaaa",*self.name1_loc)
        sleep(0.5)
        self.type_send("测试维度",*self.name2_loc)
        sleep(0.5)
        self.type_click1(*self.set_loc)


    def dimension_action2(self):
        self.type_click(*self.choice1_loc)
        sleep(1)
        self.type_click(*self.choice2_loc)

    def dimension_action3(self):
        self.type_click(*self.choice1_loc)
        sleep(1)
        self.type_click(*self.choice3_loc)

    def dimension_action4(self):
        self.type_click(*self.upload_loc)
        sleep(1)
        self.type_click(*self.set_loc)

    def dimension_action5(self):
        self.type_click(*self.authorization1_loc)
        sleep(1)
        self.type_click(*self.authorization2_loc)
        sleep(0.5)
        self.type_click(*self.share_loc)
        sleep(1)
        self.type_click(*self.sharesure_loc)

    def dimension_action6(self):
        self.type_click(*self.authorization1_loc)
        sleep(1)
        self.type_click(*self.authorization3_loc)
        sleep(1)
        self.type_click(*self.share_loc)
        sleep(1)
        self.type_click(*self.sharesure_loc)

    def dimension_action7(self):
        self.type_click(*self.label1_loc)
        sleep(1)
        self.type_click(*self.label2_loc)
        sleep(1)
        self.type_send("测试标签",*self.input_loc)
        sleep(0.5)
        self.type_click(*self.addlabel_loc)

    def dimension_action8(self):
        self.type_click(*self.deletelabel_loc)
        sleep(1)
        self.type_click1(*self.deletesure_loc)

    def dimension_action9(self):
        self.driver.refresh()
        sleep(2)
        self.type_click(*self.change_loc)
        sleep(0.5)
        self.type_send("bbbbb",*self.name1_loc)
        sleep(0.5)
        self.type_send("测试维度1",*self.name2_loc)
        sleep(0.5)
        self.type_click1(*self.set_loc)

    def dimension_action10(self):
        self.driver.refresh()
        sleep(2)
        self.type_click(*self.delete_loc)
        sleep(1)
        self.type_click1(*self.deletesure_loc)

    assert1_loc=(By.CSS_SELECTOR,".ant-message-custom-content.ant-message-success>span")
    def type_assert1(self):
        return self.find_element(*self.assert1_loc).text

    assert2_loc=(By.CSS_SELECTOR,"#main-content > div > div.scroll-content > div > div > div > div.pd2b > div > div.fleft > div.width140.iblock.ant-select.ant-select-enabled > div > div > div")
    def type_assert2(self):
        return self.find_element(*self.assert2_loc).get_attribute("title")

    assert3_loc=(By.CSS_SELECTOR,".ant-spin-nested-loading > div > div > div:nth-child(1) > div > div > span.fleft > b")
    def type_assert3(self):
        return self.find_element(*self.assert3_loc).text