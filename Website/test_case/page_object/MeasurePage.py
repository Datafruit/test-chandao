from page_object.DimensionPage import *


class MeasurePage(Page):
    #数据管理
    project_loc=(By.XPATH,'//*[text()="数据管理"]')
    #维度管理
    dimension_loc=(By.XPATH,'//*[text()="指标管理"]')
    #新建指标
    add_measure_loc=(By.CSS_SELECTOR,"#main-content > div > div.scroll-content > div > div > div > div.pd2b > div > div.fright > button.ant-btn.ant-btn-primary.iblock")
    #名称输入框
    name_loc=(By.ID,"title")
    #指标定义
    inname1_loc=(By.CSS_SELECTOR,".ant-col-19.ant-form-item-control-wrapper > div > div > div:nth-child(1) > div > div")
    inname2_loc = (By.XPATH, '//li[text()="页面名称"]')
    inname3_loc = (By.CSS_SELECTOR, ".ant-col-19.ant-form-item-control-wrapper > div > div > div.iblock.mg1l > div > div > div")
    inname4_loc = (By.XPATH, '//li[text()="去重数量"]')
    #指标条件
    addchangge1_loc=(By.CSS_SELECTOR,".ant-col-19.ant-form-item-control-wrapper > div > div > div.add-button-wrap > a")
    addchangge2_loc=(By.CSS_SELECTOR,".ant-col-19.ant-form-item-control-wrapper > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div.iblock.width140.mg1r.ant-select.ant-select-enabled > div > div")
    addchangge3_loc = (By.XPATH, '//li[text()="事件名称"]')
    addchangge4_loc=(By.CSS_SELECTOR,"div.ant-col-19.ant-form-item-control-wrapper > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div:nth-child(2) > button")
    addchangge5_loc = (By.XPATH, '//span[text()="手机概述"]')
    addchangge6_loc=(By.CSS_SELECTOR,".aligncenter.pd2b > button.ant-btn.ant-btn-primary")
    #提交
    set_loc=(By.CSS_SELECTOR,".ant-modal-footer > div > button.ant-btn.ant-btn-success.mg1r.iblock")
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
    authorization3_loc = (By.XPATH, '//li[text()="全部取消授权"]')
    #标签按钮
    label1_loc=(By.CSS_SELECTOR,"#main-content > div > div.scroll-content > div > div > div > div.pd2b > div > div.fright > div > button")
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
    change_loc=(By.CSS_SELECTOR,".sugoicon.sugo-edit.color-grey.font14.pointer.hover-color-main")
    #删除
    delete_loc=(By.CSS_SELECTOR,".sugoicon.sugo-trash.mg2l.font14.color-grey.hover-color-red.pointer")





    def measure_action1(self):
        self.type_click(*self.project_loc)
        sleep(1)
        self.type_click(*self.dimension_loc)
        sleep(1.5)
        self.type_click(*self.add_measure_loc)
        sleep(1)
        self.type_send("测试指标%s"%self.nowtime(),*self.name_loc)
        sleep(1)
        self.type_click(*self.inname1_loc)
        sleep(1)
        self.type_click(*self.inname2_loc)
        sleep(1)
        self.type_click(*self.inname3_loc)
        sleep(1)
        self.type_click(*self.inname4_loc)
        sleep(1)
        self.type_click(*self.addchangge1_loc)
        sleep(1)
        self.type_click(*self.addchangge2_loc)
        sleep(1)
        self.type_click1(*self.addchangge3_loc)
        sleep(1)
        self.type_click(*self.addchangge4_loc)
        sleep(1)
        self.type_click1(*self.addchangge5_loc)
        sleep(1)
        self.type_click(*self.addchangge6_loc)
        sleep(1)
        self.type_click(*self.set_loc)

    def measure_action2(self):
        self.driver.refresh()
        sleep(2)
        DimensionPage.dimension_action4(self)

    def measure_action3(self):
        DimensionPage.dimension_action5(self)

    def measure_action4(self):
        DimensionPage.dimension_action6(self)

    def measure_action5(self):
        DimensionPage.dimension_action7(self)

    def measure_action6(self):
        DimensionPage.dimension_action8(self)

    def measure_action7(self):
        self.driver.refresh()
        sleep(2)
        self.type_click(*self.change_loc)
        sleep(1)
        self.type_send("测试指标%s"%self.nowtime(),*self.name_loc)
        sleep(1.5)
        self.type_click(*self.set_loc)

    def measure_action8(self):
        self.driver.refresh()
        sleep(2)
        self.type_click(*self.delete_loc)
        sleep(1)
        self.type_click(*self.deletesure_loc)


#正上方提示栏封装
    assert1_loc = (By.CSS_SELECTOR, ".ant-message-custom-content.ant-message-success>span")
    def type_assert1(self):
        return self.driver.find_element(*self.assert1_loc).text

    assert3_loc=(By.CSS_SELECTOR,".ant-spin-nested-loading > div > div > div:nth-child(1) > div > div > span.fleft > b")
    def type_assert3(self):
        return self.find_element(*self.assert3_loc).text






















