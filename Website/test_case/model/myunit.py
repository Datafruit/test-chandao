import unittest
from driver.driver import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        # self.driver.quit()
        return 0
