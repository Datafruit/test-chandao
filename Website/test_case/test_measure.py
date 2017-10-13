import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.MeasurePage import MeasurePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class TestDimension(myunit.StartEnd):
    def test_measure(self):
        '''维度管理'''
        print("test_dimension start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        po1=MeasurePage(self.driver)
        po1.measure_action1()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"添加成功")
        function.insert_img(self.driver,"measure1指标创建成功.jpg")
        sleep(1)

        po1.measure_action2()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"更新成功")
        function.insert_img(self.driver,"measure2排序和隐藏.jpg")

        po1.measure_action3()
        sleep(1)
        function.insert_img(self.driver,"measure3指标全部分享.jpg")
        sleep(1)

        po1.measure_action4()
        sleep(1)
        function.insert_img(self.driver,"measure4指标全部取消分享.jpg")
        sleep(1)

        po1.measure_action5()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"添加成功")
        function.insert_img(self.driver,"measure5标签添加成功.jpg")
        sleep(1)

        po1.measure_action6()
        sleep(1)
        self.assertNotEqual(po1.type_assert3(),"测试标签")
        function.insert_img(self.driver,"measure6标签删除成功.jpg")
        sleep(1)

        po1.measure_action7()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"更新成功")
        function.insert_img(self.driver,"measure7维度更新成功9.jpg")
        sleep(1)

        po1.measure_action8()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"删除成功")
        function.insert_img(self.driver,"measure8维度删除成功10.jpg")


if __name__ == '__main__':
    unittest.main()