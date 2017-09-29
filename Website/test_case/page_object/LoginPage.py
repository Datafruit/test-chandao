from BasePage import *
from selenium.webdriver.common.by import By

class LoginPage(Page):
    url='/'
    #定位器
    username_loc=(By.ID,'username')
    password_loc=(By.ID,'password')
    submit_loc=(By.XPATH,"//button[@type='submit']")
    overview_loc=(By.XPATH, ".//*[@id='main-header']/span[1]/span/a[1]")

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)
    def type_submit(self):
        self.find_element(*self.submit_loc).click()


    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()
        sleep(2)

    loginPass_loc=(By.LINK_TEXT,'多维分析')
    loginFail_loc=(By.LINK_TEXT,'找回密码')

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        return  self.find_element(*self.loginFail_loc).text

