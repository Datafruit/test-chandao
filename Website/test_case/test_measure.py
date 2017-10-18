import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.MeasurePage import MeasurePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class TestDimension(myunit.StartEnd):
    '''指标管理'''
    def measure(self):
        po1=MeasurePage(self.driver)
        return po1

    def test_measure1(self):
        print("test_dimension start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        self.measure().measure_action1()
        self.measure().wait()
        self.assertEqual(self.measure().type_assert1(),"添加成功")
        function.insert_img(self.driver,"measure1指标创建成功.jpg")
        sleep(1)

    def test_measure2(self):
        self.measure().measure_action2()
        sleep(0.5)
        # self.measure().wait()
        self.assertEqual(self.measure().type_assert1(),"更新成功")
        function.insert_img(self.driver,"measure2排序和隐藏.jpg")
        sleep(1)

    def test_measure3(self):
        self.measure().measure_action3()
        self.measure().wait()
        self.assertEqual(self.measure().type_assert1(), "操作完成")
        function.insert_img(self.driver,"measure3指标全部授权.jpg")
        sleep(1)

    def test_measure4(self):
        self.measure().measure_action4()
        self.measure().wait()
        self.assertEqual(self.measure().type_assert1(), "操作完成")
        function.insert_img(self.driver,"measure4指标全部取消授权.jpg")
        sleep(1)

    def test_measure5(self):
        self.measure().measure_action5()
        self.measure().wait()
        self.assertEqual(self.measure().type_assert1(),"添加成功")
        function.insert_img(self.driver,"measure5标签添加成功.jpg")
        sleep(1)

    def test_measure6(self):
        self.measure().measure_action6()
        sleep(1)
        self.assertNotEqual(self.measure().type_assert3(),"测试标签")
        function.insert_img(self.driver,"measure6标签删除成功.jpg")
        sleep(1)

    def test_measure7(self):
        self.measure().measure_action7()
        self.measure().wait()
        self.assertEqual(self.measure().type_assert1(),"更新成功")
        function.insert_img(self.driver,"measure7维度更新成功.jpg")
        sleep(1)

    def test_measure8(self):
        self.measure().measure_action8()
        self.measure().wait()
        self.assertEqual(self.measure().type_assert1(),"删除成功")
        function.insert_img(self.driver,"measure8维度删除成功.jpg")


if __name__ == '__main__':
    unittest.main()