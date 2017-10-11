<<<<<<< HEAD
=======
#!/usr/bin/python
#coding:utf-8

import unittest
>>>>>>> aaa592cbf58c26b137412d00e1a483247bdec65e
from model import function,myunit
from page_object.LoginPage import *
from page_object.DashboardsPage import *
class LoginTest(myunit.StartEnd):

    def test_login1_normal(self):
        '''帐号和密码都正确'''
        print("test_login1_normal start")
        po=LoginPage(self.driver)
        po.Login_action('admin','admin12345678')
        sleep(2)

        self.assertEqual(po.type_loginPass_hint(),'多维分析')
        function.insert_img(self.driver,"220_test_login1_normal.jpg")
        print("test_login1_normal end")
    #@unittest.skip('skip this case') #跳过用例
    def test_login2_PasswdError(self):
        '''帐号或者密码不正确'''
        print("test_login2 start")
        po=LoginPage(self.driver)
        po.Login_action('admin','admin123456')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'找回密码')
        function.insert_img(self.driver,"220_test_login2_PasswdError.jpg")
        print("test_login2 end")
   # @unittest.skip('skip this case')
    def test_login3_empty(self):
        '''帐号和密码都为空'''
        print("test_login3 start")
        po = LoginPage(self.driver)
        po.Login_action('','')
        sleep(1)

        self.assertEqual(po.type_loginFail_hint(), '找回密码')
        function.insert_img(self.driver, "220_test_login3_empty.jpg")
        print("test_login3 end")


if __name__ == '__main__':
    unittest.main()