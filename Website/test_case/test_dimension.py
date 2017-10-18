import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.DimensionPage import DimensionPage

class TestDimension(myunit.StartEnd):
    '''维度管理'''
    def dimension(self):
        po1=DimensionPage(self.driver)
        return po1

    def test_dimension1(self):
        print("test_dimension start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        self.dimension().dimension_action1()
        self.dimension().wait()
        self.assertEqual(self.dimension().type_assert1(),"添加成功")
        function.insert_img(self.driver,"dimension1维度创建成功.jpg")
        sleep(1)

    def test_dimension2(self):
        self.dimension().dimension_action2()
        sleep(1)
        self.assertEqual(self.dimension().type_assert2(),"已应用维度")
        function.insert_img(self.driver,"dimension2已应用维度.jpg")
        sleep(1)

    def test_dimension3(self):
        self.dimension().dimension_action3()
        sleep(1)
        self.assertEqual(self.dimension().type_assert2(),"未应用维度")
        function.insert_img(self.driver,"dimension3未应用维度.jpg")
        sleep(1)

    def test_dimension4(self):
        self.dimension().dimension_action4()
        sleep(0.3)
        self.assertEqual(self.dimension().type_assert1(),"更新成功")
        function.insert_img(self.driver,"dimension4排序和隐藏.jpg")
        sleep(1)

    def test_dimension5(self):
        self.dimension().dimension_action5()
        self.dimension().wait()
        self.assertEqual(self.dimension().type_assert1(),"操作完成")
        function.insert_img(self.driver,"dimension5维度全部分享.jpg")
        sleep(2)

    def test_dimension6(self):
        self.dimension().dimension_action6()
        self.dimension().wait()
        self.assertEqual(self.dimension().type_assert1(),"操作完成")
        function.insert_img(self.driver,"dimension6维度全部取消分享.jpg")
        sleep(1)

    def test_dimension7(self):
        self.dimension().dimension_action7()
        self.dimension().wait()
        self.assertEqual(self.dimension().type_assert1(),"添加成功")
        function.insert_img(self.driver,"dimension7标签添加成功.jpg")
        sleep(1)

    def test_dimension8(self):
        self.dimension().dimension_action8()
        sleep(1)
        self.assertNotEqual(self.dimension().type_assert3(),"测试标签")
        function.insert_img(self.driver,"dimension8标签删除成功.jpg")
        sleep(1)

    def test_dimension9(self):
        self.dimension().dimension_action9()
        self.dimension().wait()
        self.assertEqual(self.dimension().type_assert1(),"更新成功")
        function.insert_img(self.driver,"dimension9维度更新成功.jpg")
        sleep(1)

    def test_dimensiona10(self):
        self.dimension().dimension_action10()
        self.dimension().wait()
        self.assertEqual(self.dimension().type_assert1(),"删除成功")
        function.insert_img(self.driver,"dimension10维度删除成功.jpg")

if __name__ == '__main__':
    unittest.main()