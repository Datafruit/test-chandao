import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.ProjectPage import ProjectPage

class TestProject(myunit.StartEnd):
    def test_project(self):
        '''项目管理'''
        print("test_project start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        po1=ProjectPage(self.driver)
        po1.project_action1()
        sleep(1)
        self.assertEqual(po1.type_assert2(),"测试项目")
        function.insert_img(self.driver,"project创建成功1.jpg")

        sleep(2)
        po1.project_action2()
        sleep(1)
        self.assertEqual(po1.type_assert2(),"测试项目1")
        function.insert_img(self.driver,"project修改成功2.jpg")

        sleep(2)
        po1.project_action3()
        sleep(1)
        self.assertEqual(po1.type_assert3(),"项目管理")
        function.insert_img(self.driver,"project跳转数据接入成功3.jpg")
        self.driver.back()

        sleep(2)
        po1.project_action4()
        sleep(1)
        self.assertEqual(po1.type_assert4(),"维度管理")
        function.insert_img(self.driver,"project跳转维度管理成功4.jpg")
        self.driver.back()

        sleep(2)
        po1.project_action5()
        sleep(1)
        self.assertEqual(po1.type_assert4(),"指标管理")
        function.insert_img(self.driver,"project跳转指标管理成功5.jpg")
        self.driver.back()

        sleep(2)
        po1.project_action6()
        sleep(1)
        self.assertEqual(po1.type_assert4(),"场景数据设置")
        function.insert_img(self.driver,"project跳转场景数据设置成功6.jpg")
        self.driver.back()
        self.driver.back()

        sleep(1)
        po1.project_action7()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"更新项目信息成功")
        function.insert_img(self.driver,"project分享成功7.jpg")


        sleep(1)
        po1.project_action8()
        sleep(1)
        self.assertNotEqual(po1.type_assert2(),"测试项目1")
        function.insert_img(self.driver,"project删除成功8.jpg")


if __name__ == '__main__':
    unittest.main()