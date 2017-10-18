from model import function,myunit
from page_object.RetentionPage import *
from  page_object.Choice import Choice
import unittest


class RrtentionTest(myunit.StartEnd):
    '''留存分析'''
    def retention(self):
        po1=RetentionPage(self.driver)
        return po1

    def test_retention1(self):
        print("test_retention start")
        po=Choice(self.driver)
        po.loginchoice("admin","admin12345678")
        sleep(1)
        self.retention().retention_action1("2017-07-10 00:00:00","2017-07-19 00:00:00")
        sleep(2)
        self.assertEqual(self.retention().type_assert1(),"17370")
        function.insert_img(self.driver,"retention1留存分析创建成功.jpg")
        sleep(1)

    def test_retention2(self):
        self.retention().retention_action2()
        sleep(2)
        self.assertEqual(self.retention().type_assert1(),"1861")
        function.insert_img(self.driver,"retention2留存分析保存成功.jpg")
        sleep(1)

    def test_retention3(self):
        self.retention().retention_action3()
        sleep(2)
        self.assertEqual(self.retention().type_assert1(),"1805")
        function.insert_img(self.driver,"retention3留存分析修改成功.jpg")
        sleep(1)

    def test_retention4(self):
        self.retention().retention_action4()
        # self.retention().wait()
        sleep(0.5)
        self.assertEqual(self.retention().type_assert2(),"保存成功")
        function.insert_img(self.driver,"retention4留存分析保存成功.jpg")
        sleep(1)

    def test_retention5(self):
        self.retention().retention_action5()
        # self.retention().wait()
        sleep(0.5)
        self.assertEqual(self.retention().type_assert2(),"删除成功")
        function.insert_img(self.driver,"retention5留存分析删除成功.jpg")
        sleep(2)




if __name__ == '__main__':
    unittest.main()