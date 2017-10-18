import unittest
from model import function,myunit
from page_object.SlicesPage import *
from time import sleep,strftime
from page_object.Choice import Choice

class SlicesTest(myunit.StartEnd):
    '''单图'''
    def slices(self):
        po1=SlicesPage(self.driver)
        return po1

    def test_slices1(self):
        po=Choice(self.driver)
        po.loginchoice('admin','admin12345678')
        sleep(1)
        self.slices().slices_action1('测试单图')
        sleep(2)
        self.assertEqual(self.slices().type_titileslices(),"保存成功!查看单图")
        function.insert_img(self.driver, "slices1单图保存成功.jpg")
        sleep(1)

    def test_slices2(self):
        self.slices().slices_action2()
        sleep(2)
        self.assertEqual(self.slices().type_allslices(),"设置成功")
        function.insert_img(self.driver, "slices2单图授权成功.jpg")
        self.driver.refresh()
        sleep(2)

    def test_slices3(self):
        self.slices().slices_action3()
        sleep(1)
        self.assertEqual(self.slices().type_allslices(),"加入概览成功")
        function.insert_img(self.driver, "slices3单图加入概览成功.jpg")
        self.driver.refresh()
        sleep(2)

    def test_slices4(self):
        self.slices().slices_action4()
        sleep(1)
        self.assertEqual(self.slices().type_allslices(),"订阅成功")
        function.insert_img(self.driver, "slices4单图订阅成功.jpg")

    def test_slices5(self):
        self.slices().slices_action5()
        sleep(2)
        function.insert_img(self.driver, "slices5单图删除成功.jpg")
        print("test_slices5 end")


if __name__ == '__main__':
    unittest.main()