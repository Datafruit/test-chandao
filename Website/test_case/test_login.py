from model import function,myunit
from page_object.LoginPage import *
from page_object.DashboardsPage import *
import unittest
class LoginTest(myunit.StartEnd):
    '''登录验证'''
    def test_login3_normal(self):
        '''帐号和密码都正确'''
        po=LoginPage(self.driver)
        po.Login_action('admin','admin12345678')
        sleep(1)

        self.assertEqual(po.type_loginPass_hint(),'多维分析')
        function.insert_img(self.driver,"login3登录成功.jpg")
    #@unittest.skip('skip this case') #跳过用例
    def test_login2_PasswdError(self):
        '''帐号或者密码不正确'''
        po=LoginPage(self.driver)
        po.Login_action('admin','admin123456')
        sleep(1)

        self.assertEqual(po.type_loginFail_hint(),'找回密码')
        function.insert_img(self.driver,"login2登录时密码为空.jpg")
   # @unittest.skip('skip this case')
    def test_login1_empty(self):
        '''帐号和密码都为空'''
        po = LoginPage(self.driver)
        po.Login_action('','')
        sleep(1)

        self.assertEqual(po.type_loginFail_hint(), '找回密码')
        function.insert_img(self.driver, "login1登陆时帐号密码为空.jpg")


if __name__ == '__main__':
    unittest.main()