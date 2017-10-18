import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.ProjectPage import ProjectPage

class TestProject(myunit.StartEnd):
    '''项目管理'''
    def project(self):
        po1=ProjectPage(self.driver)
        return po1

    def test_project1(self):
        print("test_project start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        self.project().project_action1()
        sleep(1)
        self.assertEqual(self.project().type_assert2(),"测试项目")
        function.insert_img(self.driver,"project1创建成功.jpg")
        sleep(1)

    def test_project2(self):
        self.project().project_action2()
        sleep(1)
        self.assertEqual(self.project().type_assert2(),"测试项目1")
        function.insert_img(self.driver,"project2修改成功.jpg")
        sleep(2)

    def test_project3(self):
        self.project().project_action3()
        sleep(1)
        self.assertEqual(self.project().type_assert3(),"项目管理")
        function.insert_img(self.driver,"project3跳转数据接入成功.jpg")
        self.driver.back()
        sleep(2)

    def test_project4(self):
        self.project().project_action4()
        sleep(1)
        self.assertEqual(self.project().type_assert4(),"维度管理")
        function.insert_img(self.driver,"project4跳转维度管理成功.jpg")
        self.driver.back()

    def test_project5(self):
        sleep(2)
        self.project().project_action5()
        sleep(1)
        self.assertEqual(self.project().type_assert4(),"指标管理")
        function.insert_img(self.driver,"project5跳转指标管理成功.jpg")
        self.driver.back()
        sleep(2)

    def test_project6(self):
        self.project().project_action6()
        sleep(1)
        self.assertEqual(self.project().type_assert4(),"场景数据设置")
        function.insert_img(self.driver,"project6跳转场景数据设置成功.jpg")
        self.driver.back()
        self.driver.back()
        sleep(1)

    def test_project7(self):
        self.project().project_action7()
        sleep(1)
        self.assertEqual(self.project().type_assert1(),"更新项目信息成功")
        function.insert_img(self.driver,"project7分享成功.jpg")
        sleep(1)

    def test_project8(self):
        self.project().project_action8()
        sleep(1)
        self.assertNotEqual(self.project().type_assert2(),"测试项目1")
        function.insert_img(self.driver,"project8删除成功.jpg")


if __name__ == '__main__':
    unittest.main()