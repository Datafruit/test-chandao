import unittest
from model import function,myunit
from page_object.LoginPage import *
from page_object.Choice import *
from test_login import LoginTest

class LoginandChoice(myunit.StartEnd):
    def test_loginchoice(self):
        po=LoginPage(self.driver)
        po.Login_action('admin','admin12345678')
        po1=Choice(self.driver)
        po1.choice()
        sleep(2)





if __name__ == '__main__':
    unittest.main()
