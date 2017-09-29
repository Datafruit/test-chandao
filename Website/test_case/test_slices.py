import unittest
from model import function,myunit
from page_object.SlicesPage import *
from time import sleep,strftime
from page_object.Choice import Choice

class SlicesTest(myunit.StartEnd):
    # def test_slices1(self):
    #     '''新建单图'''
    #     print("test_slices1 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(2)
    #     po1=SlicesPage(self.driver)
    #     po1.slices_action1('测试单图')
    #     sleep(2)
    #     self.assertEqual(po1.type_titileslices(),"保存成功!查看单图")
    #     function.insert_img(self.driver, "220_test_slices1.jpg")
    #     print("test_slices1 end")
    #
    # def test_slices2(self):
    #     '''分享单图'''
    #     print("test_slices2 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(2)
    #     po1=SlicesPage(self.driver)
    #     po1.slices_action2()
    #     sleep(2)
    #     self.assertEqual(po1.type_allslices(),"设置成功")
    #     function.insert_img(self.driver, "220_test_slices2.jpg")
    #     print("test_slices2 end")
    #
    # def test_slices3(self):
    #     '''单图加入概览'''
    #     print("test_slices3 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(2)
    #     po1=SlicesPage(self.driver)
    #     po1.slices_action3()
    #     sleep(2)
    #     self.assertEqual(po1.type_allslices(),"加入概览成功")
    #     function.insert_img(self.driver, "220_test_slices3.jpg")
    #     print("test_slices2 end")
    #
    # def test_slices4(self):
    #     '''单图订阅'''
    #     print("test_slices4 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(2)
    #     po1=SlicesPage(self.driver)
    #     po1.slices_action4()
    #     sleep(2)
    #     self.assertEqual(po1.type_allslices(),"订阅成功")
    #     function.insert_img(self.driver, "220_test_slices4.jpg")
    #     print("test_slices4 end")
    #
    # def test_slices5(self):
    #     '''单图删除'''
    #     print("test_slices5 start")
    #     po=Choice(self.driver)
    #     po.loginchoice('admin','admin12345678')
    #     sleep(2)
    #     po1=SlicesPage(self.driver)
    #     po1.slices_action5()
    #     sleep(2)
    #     function.insert_img(self.driver, "220_test_slices5.jpg")
    #     print("test_slices5 end")

    def test_slices6(self):
        '''集合版'''
        print("test_slices6 start")
        po=Choice(self.driver)
        po.loginchoice('admin','admin12345678')
        sleep(2)
        po1=SlicesPage(self.driver)
        po1.slices_action1('测试单图')
        sleep(2)
        self.assertEqual(po1.type_titileslices(),"保存成功!查看单图")
        function.insert_img(self.driver, "220_test_slices1.jpg")
        sleep(1)

        po1.slices_action2()
        sleep(2)
        self.assertEqual(po1.type_allslices(),"设置成功")
        function.insert_img(self.driver, "220_test_slices2.jpg")

        self.driver.refresh()
        sleep(2)
        po1.slices_action3()
        sleep(1)
        self.assertEqual(po1.type_allslices(),"加入概览成功")
        function.insert_img(self.driver, "220_test_slices3.jpg")

        self.driver.refresh()
        sleep(2)
        po1.slices_action4()
        sleep(1)
        self.assertEqual(po1.type_allslices(),"订阅成功")
        function.insert_img(self.driver, "220_test_slices4.jpg")

        po1.slices_action5()
        sleep(2)
        function.insert_img(self.driver, "220_test_slices5.jpg")
        print("test_slices5 end")


if __name__ == '__main__':
    unittest.main()