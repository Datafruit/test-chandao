import unittest
from  driver.driver import *

class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        # return 0
