from page_object.LoginPage import *

class Choice(Page):
    selection_loc=(By.XPATH,".//*[@id='main-header']/span[2]/div/div/div")
    active_loc=(By.XPATH,"//*[text()='数果手机产品库数据测试']")

    def choice(self):
        self.find_element(*self.selection_loc).click()
        sleep(0.5)
        self.find_element(*self.active_loc).click()

    def loginchoice(self,username,password):
        po=LoginPage(self.driver)
        po.Login_action(username,password)
        sleep(1)
        po1=Choice(self.driver)
        po1.choice()

