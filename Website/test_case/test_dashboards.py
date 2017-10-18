import unittest
from model import function,myunit
from page_object.DashboardsPage import *
from time import sleep
from page_object.Choice import Choice


class DashboardsTest(myunit.StartEnd):
    '''数据看板'''
    def dashboards(self):
        po1=DashboardsPage(self.driver)
        return po1

    def test_dashboards1(self):
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        self.dashboards().dashboards_action1()
        sleep(0.5)
        # self.dashboards().wait()
        self.assertEqual(self.dashboards().dashboards_pass(),"添加成功")
        function.insert_img(self.driver,"dashboards1数据看板创建成功.jpg")
        sleep(1)

    def test_dashboards2(self):
        self.dashboards().dashboards_action2()
        # self.dashboards().wait()
        sleep(0.5)
        self.assertEqual(self.dashboards().dashboards_pass(),"修改成功")
        function.insert_img(self.driver,"dashboards2数据看板修改成功.jpg")
        sleep(1)

    def test_dashboards3(self):
        self.dashboards().dashboards_action3()
        self.dashboards().wait()
        self.assertEqual(self.dashboards().dashboards_pass(),"设置成功")
        function.insert_img(self.driver,"dashboards3数据看板分享成功.jpg")
        self.driver.refresh()
        sleep(1.5)

    # def test_dashboards4(self):
    #     self.dashboards().dashboards_action4()
    #     self.dashboards().wait()
    #     self.assertEqual(self.dashboards().dashboards_pass(), "订阅成功")
    #     function.insert_img(self.driver, "dashboards4数据看板订阅成功.jpg")
    #     self.driver.refresh()
    #     sleep(1.5)

    def test_dashboards5(self):
        self.dashboards().dashboards_action5()
        # self.dashboards().wait()
        sleep(0.5)
        self.assertEqual(self.dashboards().dashboards_pass(),"删除成功")
        function.insert_img(self.driver,"dashboards5数据看板删除成功.jpg")

    def test_dashboards6(self):
        self.dashboards().dashboards_action6()
        sleep(2)

        self.assertEqual(self.dashboards().dashboards_error(), "保存看板")
        function.insert_img(self.driver, "dashboards6数据看板名称为空保存失败.jpg")




if __name__ == '__main__':
    unittest.main()


