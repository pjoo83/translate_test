import unittest
from base.get_driver import GetDriver
import warnings


class TestingCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.getDriver = GetDriver()


    # def tearDown(self):
    #     # pass
    #     # GetDriver.close_page()
    #     self.getDriver.close_page()
