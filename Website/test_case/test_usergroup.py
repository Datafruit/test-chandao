import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.UsergroupPage import UsergroupPage

class Test_Usergroup(myunit.StartEnd):
    def test_usergroup1(self):
        '''用户分群测试'''
        print("test_usergroup1 start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        po1=UsergroupPage(self.driver)
        po1.usergroup_action1("测试分群","2017-07-15 00:00:00","2017-07-17 23:59:59")
        sleep(2)

        self.assertEqual(po1.type_message(),"添加分群成功")
        self.assertEqual(po1.type_number(),"102")
        function.insert_img(self.driver,"分群添加成功截图.jpg")

        sleep(2)
        po1.usergroup_action2()
        sleep(2)
        self.assertEqual(po1.type_message(),"更新成功")
        self.assertEqual(po1.type_number(),"10")
        function.insert_img(self.driver, "分群更新成功截图.jpg")
        print("test_usergroup1 end")

        self.driver.back()
        sleep(0.5)
        self.driver.back()

        sleep(2)
        po1.usergroup_action3()
        sleep(1)
        self.assertEqual(po1.type_choice11(),"保存为常用路径")
        function.insert_img(self.driver,"跳转路劲分析截图.jpg")
        self.driver.back()

        sleep(2)
        po1.usergroup_action4()
        sleep(1)
        self.assertEqual(po1.type_choice21(),"保存为常用留存")
        function.insert_img(self.driver,"跳转留存分析截图.jpg")
        self.driver.back()

        sleep(2)
        po1.usergroup_action5()
        sleep(1)
        self.assertEqual(po1.type_choice31(),"保 存")
        function.insert_img(self.driver,"跳转漏斗分析截图.jpg")

        sleep(1)
        po1.usergroup_action6()
        sleep(1)
        self.assertEqual(po1.type_choice41(),"保存常用事件")
        function.insert_img(self.driver,"跳转事件分析截图.jpg")
        self.driver.back()

        sleep(1)
        po1.usergroup_action7()
        sleep(1.5)
        self.assertEqual(po1.type_seeuser1(),"用户细查")
        function.insert_img(self.driver,"跳转用户细查截图.jpg")
        self.driver.back()

        sleep(1)
        po1.usergroup_action8()
        sleep(1)
        self.assertEqual(po1.type_updateuser1(),"更 新")
        function.insert_img(self.driver,"跳转编辑截图.jpg")
        self.driver.back()

        sleep(1)
        po1.usergroup_action9()
        sleep(1)
        function.insert_img(self.driver,"删除后截图.jpg")

if __name__ == '__main__':
    unittest.main()