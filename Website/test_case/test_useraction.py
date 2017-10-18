import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.UseractionPage import UseractionPage



class Test_Useraction(myunit.StartEnd):
    '''事件分析'''
    def useraction(self):
        po1=UseractionPage(self.driver)
        return po1

    def test_useraction1(self):
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        self.useraction().useraction_action1()
        sleep(1)
        self.assertEqual(self.useraction().type_assert1(),"61615")
        function.insert_img(self.driver,"action1事件分析总次数.jpg")


    def test_useraction2(self):
        self.useraction().useraction_action2()
        sleep(1)

        self.assertEqual(self.useraction().type_assert1(),"9736")
        function.insert_img(self.driver,"action2事件分析总人数.jpg")


    def test_useraction3(self):
        self.useraction().useraction_action3()
        sleep(1)
        self.assertEqual(self.useraction().type_assert1(),"2.70")
        function.insert_img(self.driver,"action3事件分析平均次数.jpg")


    def test_useraction4(self):
        self.useraction().useraction_action4()
        sleep(1)
        self.assertEqual(self.useraction().type_assert1(),"6.33")
        function.insert_img(self.driver,"action4事件分析人均次数.jpg")


    def test_useraction5(self):
        self.useraction().useraction_action5()
        sleep(1)
        self.assertEqual(self.useraction().type_assert1(),"467840.90")
        function.insert_img(self.driver,"action5事件分析总时长.jpg")


    def test_useraction6(self):
        self.useraction().useraction_action6()
        sleep(1)
        self.assertEqual(self.useraction().type_assert1(),"20.47")
        function.insert_img(self.driver,"action6事件分析平均浏览时长.jpg")


    def test_useraction7(self):
        self.useraction().useraction_action7()
        sleep(1)
        self.assertEqual(self.useraction().type_assert1(),"48.05")
        function.insert_img(self.driver,"action7事件分析人均浏览时长.jpg")


    def test_useraction8(self):
        self.useraction().useraction_action8()
        sleep(1)
        self.assertEqual(self.useraction().type_assert2(),"168")
        function.insert_img(self.driver,"action8事件分析选择全部事件.jpg")
        sleep(1)

    def test_useraction9(self):
        self.useraction().useraction_action9()
        sleep(1)
        function.insert_img(self.driver,"action9事件分析饼图.jpg")
        sleep(1)

    def test_useractiona10(self):
        self.useraction().useraction_action10()
        sleep(1)
        function.insert_img(self.driver,"action10事件分析一维柱图.jpg")
        sleep(1)

    def test_useractiona11(self):
        self.useraction().useraction_action11()
        sleep(1)
        function.insert_img(self.driver,"action11事件分析一维面积图.jpg")
        sleep(1)

    def test_useractiona12(self):
        self.useraction().useraction_action12()
        sleep(0.5)
        # self.useraction().wait()
        self.assertEqual(self.useraction().type_assert3(),"保存成功")
        function.insert_img(self.driver,"action12事件分析保存成功.jpg")
        sleep(1)

    def test_useractiona13(self):
        self.useraction().useraction_action13()
        # self.useraction().wait()
        sleep(0.5)
        self.assertEqual(self.useraction().type_assert3(),"删除成功")
        function.insert_img(self.driver,"action13事件分析删除成功.jpg")




if __name__ == '__main__':
    unittest.main()