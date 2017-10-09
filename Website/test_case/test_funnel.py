#coding:utf-8

from time import sleep
from model import function,myunit
from page_object.FunnelPage import *
import unittest
from page_object.Choice import *

class FunnelTest(myunit.StartEnd):
    def test_funnel(self):
        '''漏斗分析--5个案例'''
        print("test_retention start")
        po=Choice(self.driver)
        po.loginchoice("admin","admin12345678")
        sleep(1)

        po1=FunnelPage(self.driver)
        po1.funnel_action1()
        sleep(2)
        # self.assertEqual(po1.type_assert3(), "25543")
        # function.insert_img(self.driver, "创建成功.jpg")

        # po1.funnel_action2()
        # sleep(0.7)
        # self.assertEqual(po1.type_assert1(),"保存成功")
        # function.insert_img(self.driver,"保存成功.jpg")

        # sleep(1)
        # po1.funnel_action3()
        # sleep(0.7)
        # self.assertEqual(po1.type_assert1(),"保存成功")
        # function.insert_img(self.driver,"更新成功.jpg")
        #
        # sleep(1)
        # po1.funnel_action4()
        # sleep(1.5)
        # self.assertEqual(po1.type_assert2(),"用户细查")
        # function.insert_img(self.driver,"跳转用户细查.jpg")
        # self.driver.back()
        #
        # sleep(2)
        # po1.funnel_action5()
        # sleep(0.7)
        # self.assertEqual(po1.type_assert1(),"删除成功")
        # function.insert_img(self.driver,"删除成功.jpg")

if __name__ == '__main__':
    unittest.main()