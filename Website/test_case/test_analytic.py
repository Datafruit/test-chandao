from time import sleep
from model import myunit,function
from page_object.Choice import *
from page_object.AnalyticPage import *
import unittest

class Test_analytic(myunit.StartEnd):
    '''多维分析'''
    def test_analytic1(self):
        print("test_analytic start")
        po=Choice(self.driver)
        po.loginchoice('admin','admin12345678')
        sleep(2)
        po1=AnalyticPage(self.driver)
        po1.analytic_action1()
        sleep(2)

        self.assertEqual(po1.type_assert1(),"手机平台首页")
        self.assertEqual(po1.type_assert2(),"7,874")
        function.insert_img(self.driver,'anaalytic多维分析.jpg')
        print("test_analytic end")


if __name__ == '__main__':
    unittest.main()