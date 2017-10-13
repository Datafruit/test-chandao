import unittest
from model import myunit,function
from page_object.Choice import Choice
from time import sleep
from page_object.MeasurePage import MeasurePage

class TestDimension(myunit.StartEnd):
    def test_measure(self):
        '''维度管理'''
        print("test_dimension start")
        po = Choice(self.driver)
        po.loginchoice('admin', 'admin12345678')
        sleep(1)
        po1=MeasurePage(self.driver)
        po1.measure_action1()
        sleep(1)

        po1.measure_action2()
        sleep(1)

        po1.measure_action3()
        sleep(1)

        po1.measure_action4()
        sleep(1)

        po1.measure_action5()
        sleep(1)

        po1.measure_action6()
        sleep(1)




if __name__ == '__main__':
    unittest.main()