import unittest
from  driver import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.maximize_window()

    def tearDown(self):
         # self.driver.quit()
        return 0
