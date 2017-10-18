
from model import function,myunit
from page_object.FunnelPage import *
import unittest
from page_object.Choice import *

class FunnelTest(myunit.StartEnd):
    '''漏斗分析'''
    def funnel(self):
        po1=FunnelPage(self.driver)
        return po1
    def test_funnel1(self):
        print("test_retention start")
        po=Choice(self.driver)
        po.loginchoice("admin","admin12345678")
        sleep(1)
        self.funnel().funnel_action1()
        sleep(2)
        self.assertEqual(self.funnel().type_assert3(), "25543")
        function.insert_img(self.driver, "funnel1漏斗创建成功.jpg")
        sleep(1)

    def test_funnel2(self):
        self.funnel().funnel_action2()
        # self.funnel().wait()
        sleep(0.7)
        self.assertEqual(self.funnel().type_assert1(),"保存成功")
        function.insert_img(self.driver,"funnel2漏斗保存成功.jpg")
        sleep(1)

    def test_funnel3(self):
        sleep(1)
        self.funnel().funnel_action3()
        # self.funnel().wait()
        sleep(1)
        self.assertEqual(self.funnel().type_assert1(),"保存成功")
        function.insert_img(self.driver,"funnel3漏斗更新成功.jpg")
        sleep(1)

    def test_funnel4(self):
        sleep(1)
        self.funnel().funnel_action4()
        sleep(1)
        self.assertEqual(self.funnel().type_assert2(),"用户细查")
        function.insert_img(self.driver,"funnel4漏斗跳转用户细查.jpg")
        self.driver.back()
        sleep(1)

    def test_funnel5(self):
        sleep(2)
        self.funnel().funnel_action5()
        # self.funnel().wait()
        sleep(0.5)
        self.assertEqual(self.funnel().type_assert1(),"删除成功")
        function.insert_img(self.driver,"funnel5漏斗删除成功.jpg")

if __name__ == '__main__':
    unittest.main()