import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.DimensionPage import DimensionPage

class TestDimension(myunit.StartEnd):
    def test_dimension(self):
        '''维度管理'''
        print("test_dimension start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        po1=DimensionPage(self.driver)
        po1.dimension_action1()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"添加成功")
        function.insert_img(self.driver,"dimension维度创建成功1.jpg")

        sleep(2)
        po1.dimension_action2()
        sleep(1)
        self.assertEqual(po1.type_assert2(),"已应用维度")
        function.insert_img(self.driver,"dimension已应用维度2.jpg")

        sleep(2)
        po1.dimension_action3()
        sleep(1)
        self.assertEqual(po1.type_assert2(),"未应用维度")
        function.insert_img(self.driver,"dimension未应用维度3.jpg")

        sleep(2)
        po1.dimension_action4()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"更新成功")
        function.insert_img(self.driver,"dimension排序和隐藏4.jpg")

        sleep(2)
        po1.dimension_action5()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"操作完成")
        function.insert_img(self.driver,"dimension维度全部分享5.jpg")

        sleep(2)
        po1.dimension_action6()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"操作完成")
        function.insert_img(self.driver,"dimension维度全部取消分享6.jpg")

        sleep(2)
        po1.dimension_action7()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"添加成功")
        function.insert_img(self.driver,"dimension标签添加成功7.jpg")

        po1.dimension_action8()
        sleep(1)
        self.assertNotEqual(po1.type_assert3(),"测试标签")
        function.insert_img(self.driver,"dimension标签删除成功8.jpg")

        sleep(2)
        po1.dimension_action9()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"更新成功")
        function.insert_img(self.driver,"dimension维度更新成功9.jpg")

        sleep(2)
        po1.dimension_action10()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"删除成功")
        function.insert_img(self.driver,"dimension维度删除成功10.jpg")

if __name__ == '__main__':
    unittest.main()