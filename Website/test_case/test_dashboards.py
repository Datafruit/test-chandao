import unittest
from model import function,myunit
from page_object.DashboardsPage import *
from time import sleep
from page_object.Choice import Choice


class DashboardsTest(myunit.StartEnd):
    # def test_dashboards1(self):
    #     '''新增数据看板测试'''
    #     print("test_dashboards1 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(2)
    #     po1=DashboardsPage(self.driver)
    #     po1.dashboards_action1('测试看板')
    #     sleep(1)
    #
    #     self.assertEqual(po1.dashboards_pass(),"添加成功")
    #     function.insert_img(self.driver,"220_test_dashboards1.jpg")
    #     print("test_dashboards1 end")
    #
    # def test_dashboards2(self):
    #     '''数据看板编辑'''
    #     print("test_dashboards1 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(1)
    #     po1=DashboardsPage(self.driver)
    #     po1.dashboards_action2()
    #     sleep(0.5)
    #
    #     self.assertEqual(po1.dashboards_pass(),"修改成功")
    #     function.insert_img(self.driver,"220_test_dashboards2.jpg")
    #     print("test_dashboards1 end")
    # def test_dashboards3(self):
    #     '''数据看板分享'''
    #     print("test_dashboards1 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(1)
    #     po1=DashboardsPage(self.driver)
    #     po1.dashboards_action3()
    #     sleep(2)
    #
    #     self.assertEqual(po1.dashboards_pass(),"设置成功")
    #     function.insert_img(self.driver,"220_test_dashboards3.jpg")
    #     print("test_dashboards1 end")
    #
    # def test_dashboards4(self):
    #     '''数据看板订阅'''
    #     print("test_dashboards1 start")
    #     po = Choice(self.driver)
    #     po.loginchoice('admin', 'admin12345678')
    #     sleep(1)
    #     po1 = DashboardsPage(self.driver)
    #     po1.dashboards_action4()
    #     sleep(2)
    #
    #     self.assertEqual(po1.dashboards_pass(), "订阅成功")
    #     function.insert_img(self.driver, "220_test_dashboards4.jpg")
    #     print("test_dashboards1 end")
    #
    # def test_dashboards5(self):
    #     '''数据看板删除'''
    #     print("test_dashboards1 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(1)
    #     po1=DashboardsPage(self.driver)
    #     po1.dashboards_action5()
    #     sleep(0.5)
    #
    #     self.assertEqual(po1.dashboards_pass(),"删除成功")
    #     function.insert_img(self.driver,"220_test_dashboards5.jpg")
    #     print("test_dashboards1 end")
    #
    # def test_dashboards6(self):
    #     '''数据看板没有单图时保存'''
    #     print("test_dashboards6 start")
    #     po = Choice(self.driver)
    #     po.loginchoice('admin', 'admin12345678')
    #     sleep(1)
    #     po1 = DashboardsPage(self.driver)
    #     po1.dashboards_action6("测试看板")
    #     sleep(2)
    #
    #     self.assertEqual(po1.dashboards_error(), "保存看板")
    #     function.insert_img(self.driver, "220_test_dashboards6.jpg")
    #     print("test_dashboards6 end")

    def test_dashboards7(self):
        '''集合版'''
        print("test_dashboards7 start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        po1=DashboardsPage(self.driver)
        po1.dashboards_action1('测试看板')
        sleep(1)

        self.assertEqual(po1.dashboards_pass(),"添加成功")
        function.insert_img(self.driver,"220_test_dashboards1.jpg")


        po1.dashboards_action2()
        sleep(1)

        self.assertEqual(po1.dashboards_pass(),"修改成功")
        function.insert_img(self.driver,"220_test_dashboards2.jpg")

        po1.dashboards_action3()
        sleep(1)

        self.assertEqual(po1.dashboards_pass(),"设置成功")
        function.insert_img(self.driver,"220_test_dashboards3.jpg")


        self.driver.refresh()
        sleep(1.5)
        po1.dashboards_action4()
        sleep(1)

        self.assertEqual(po1.dashboards_pass(), "订阅成功")
        function.insert_img(self.driver, "220_test_dashboards4.jpg")

        self.driver.refresh()
        sleep(1.5)
        po1.dashboards_action5()
        sleep(1)

        self.assertEqual(po1.dashboards_pass(),"删除成功")
        function.insert_img(self.driver,"220_test_dashboards5.jpg")


        po1.dashboards_action6("测试看板")
        sleep(2)

        self.assertEqual(po1.dashboards_error(), "保存看板")
        function.insert_img(self.driver, "220_test_dashboards6.jpg")
        print("test_dashboards7 end")



if __name__ == '__main__':
    unittest.main()


