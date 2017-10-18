import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.UsergroupPage import UsergroupPage

class Test_Usergroup(myunit.StartEnd):
    '''用户分群'''
    def usergroup(self):
        po1=UsergroupPage(self.driver)
        return po1

    def test_usergroup1(self):
        '''用户分群测试'''
        print("test_usergroup1 start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        self.usergroup().usergroup_action1()
        self.usergroup().wait()
        self.assertEqual(self.usergroup().type_message(),"添加分群成功")
        self.assertEqual(self.usergroup().type_number(),"119")
        function.insert_img(self.driver,"usergroup1分群添加成功截图.jpg")
        sleep(2)

    def test_usergroup2(self):
        self.usergroup().usergroup_action2()
        self.usergroup().wait()
        self.assertEqual(self.usergroup().type_message(),"更新成功")
        self.assertEqual(self.usergroup().type_number(),"12")
        function.insert_img(self.driver, "usergroup2分群更新成功截图.jpg")
        self.driver.back()
        sleep(0.5)
        self.driver.back()
        sleep(1)

    def test_usergroup3(self):
        self.usergroup().usergroup_action3()
        sleep(1)
        self.assertEqual(self.usergroup().type_choice11(),"保存为常用路径")
        function.insert_img(self.driver,"usergroup3跳转路劲分析截图.jpg")
        self.driver.back()
        sleep(1)

    def test_usergroup4(self):
        self.usergroup().usergroup_action4()
        sleep(1)
        self.assertEqual(self.usergroup().type_choice21(),"保存为常用留存")
        function.insert_img(self.driver,"usergroup4跳转留存分析截图.jpg")
        self.driver.back()
        sleep(1)

    def test_usergroup5(self):
        self.usergroup().usergroup_action5()
        sleep(1)
        self.assertEqual(self.usergroup().type_choice31(),"保 存")
        function.insert_img(self.driver,"usergroup5跳转漏斗分析截图.jpg")
        sleep(1)

    def test_usergroup6(self):
        self.usergroup().usergroup_action6()
        sleep(1)
        self.assertEqual(self.usergroup().type_choice41(),"保存常用事件")
        function.insert_img(self.driver,"usergroup6跳转事件分析截图.jpg")
        self.driver.back()
        sleep(1)

    def test_usergroup7(self):
        self.usergroup().usergroup_action7()
        sleep(1.5)
        self.assertEqual(self.usergroup().type_seeuser1(),"用户细查")
        function.insert_img(self.driver,"usergroup7跳转用户细查截图.jpg")
        self.driver.back()
        sleep(1)

    def test_usergroup8(self):
        self.usergroup().usergroup_action8()
        sleep(1)
        self.assertEqual(self.usergroup().type_updateuser1(),"更 新")
        function.insert_img(self.driver,"usergroup8跳转编辑截图.jpg")
        self.driver.back()
        sleep(1)

    def test_usergroup9(self):
        self.usergroup().usergroup_action9()
        sleep(1)
        function.insert_img(self.driver,"usergroup9删除后截图.jpg")

if __name__ == '__main__':
    unittest.main()