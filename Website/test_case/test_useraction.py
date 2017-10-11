import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.UseractionPage import UseractionPage



class Test_Useraction(myunit.StartEnd):
    def test_usergroup1(self):
        '''事件分析'''
        print("test_usergroup1 start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        po1=UseractionPage(self.driver)
        po1.useraction_action1()

        self.assertEqual(po1.type_assert1(),"61615")
        function.insert_img(self.driver,"action总次数验证1.jpg")

        sleep(1)
        po1.useraction_action2()
        sleep(1)

        self.assertEqual(po1.type_assert1(),"9736")
        function.insert_img(self.driver,"action总人数验证2.jpg")

        sleep(1)
        po1.useraction_action3()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"2.70")
        function.insert_img(self.driver,"action平均次数验证3.jpg")

        sleep(1)
        po1.useraction_action4()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"6.33")
        function.insert_img(self.driver,"action人均次数验证4.jpg")


        sleep(1)
        po1.useraction_action5()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"467840.90")
        function.insert_img(self.driver,"action总时长验证5.jpg")


        sleep(1)
        po1.useraction_action6()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"20.47")
        function.insert_img(self.driver,"action平均浏览时长验证6.jpg")


        sleep(1)
        po1.useraction_action7()
        sleep(1)
        self.assertEqual(po1.type_assert1(),"48.05")
        function.insert_img(self.driver,"action人均浏览时长验证7.jpg")


        sleep(1)
        po1.useraction_action8()
        sleep(1)
        self.assertEqual(po1.type_assert2(),"168")
        function.insert_img(self.driver,"action选择全部事件验证8.jpg")


        sleep(1)
        po1.useraction_action9()
        sleep(1)
        function.insert_img(self.driver,"action饼图验证9.jpg")

        sleep(1)
        po1.useraction_action10()
        sleep(1)
        function.insert_img(self.driver,"action一维柱图验证10.jpg")

        sleep(1)
        po1.useraction_action11()
        sleep(1)
        function.insert_img(self.driver,"action一维面积图验证11.jpg")

        sleep(1)
        po1.useraction_action12()
        sleep(1)
        self.assertEqual(po1.type_assert3(),"保存成功")
        function.insert_img(self.driver,"action保存成功验证12.jpg")


        sleep(1)
        po1.useraction_action13()
        sleep(1)
        self.assertEqual(po1.type_assert3(),"删除成功")
        function.insert_img(self.driver,"action删除成功验证13.jpg")




if __name__ == '__main__':
    unittest.main()