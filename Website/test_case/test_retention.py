from model import function,myunit
from page_object.RetentionPage import *
from  page_object.Choice import Choice
import unittest


class RrtentionTest(myunit.StartEnd):
    def test_retention(self):
        '''留存分析--5个案例'''
        print("test_retention start")
        po=Choice(self.driver)
        po.loginchoice("admin","admin12345678")
        sleep(1)
        po1=RetentionPage(self.driver)
        po1.retention_action1("2017-07-10 00:00:00","2017-07-19 00:00:00")
        sleep(2)

        self.assertEqual(po1.type_assert1(),"17370")
        function.insert_img(self.driver,"留存分析1截图.jpg")
        sleep(2)

        po1.retention_action2()
        sleep(2)

        self.assertEqual(po1.type_assert1(),"1861")
        function.insert_img(self.driver,"留存分析2截图.jpg")
        sleep(2)

        po1.retention_action3()
        sleep(2)

        self.assertEqual(po1.type_assert1(),"1805")
        function.insert_img(self.driver,"留存分析3截图.jpg")
        sleep(2)

        po1.retention_action4()
        sleep(1)
        self.assertEqual(po1.type_assert2(),"保存成功")
        function.insert_img(self.driver,"留存分析4截图.jpg")
        sleep(2)

        po1.retention_action5()
        sleep(1)
        self.assertEqual(po1.type_assert2(),"删除成功")
        function.insert_img(self.driver,"留存分析5截图.jpg")
        sleep(2)




if __name__ == '__main__':
    unittest.main()