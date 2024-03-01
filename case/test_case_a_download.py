from base.testing import TestingCase
from base.base import Base
import time
from base.check_tools import change_filename
from page.page_element import Test_language
import unittest

el = Test_language()


class TeslFlowDownload(TestingCase):

    def test_download(self):
        """
             进行多语言文件下载
        """
        self.getDriver.create_driver()
        self.getDriver.open_page(el.login_url)
        self.driver = Base(self.getDriver.driver)
        self.driver.wait_time(el.uname)
        # 登陆
        # time.sleep(1)
        self.driver.base_click(el.close_cookie)
        time.sleep(2)
        self.driver.base_input(el.uname, "translator.aa@ushow.media")
        self.driver.base_input(el.pwd, "Re4@12345")
        self.driver.base_click(el.login)
        self.driver.wait_time(el.open)

        self.driver.base_click(el.open)
        time.sleep(5)
        self.driver.wait_time(el.android)
        self.driver.base_click(el.android)
        self.driver.base_click(el.language)
        # 统一下载安卓和IOS
        self.getDriver.open_page(url=el.download_android)
        time.sleep(10)
        change_filename("android")
        self.getDriver.open_page(url=el.download_ios)
        time.sleep(10)
        change_filename("ios")
        self.getDriver.open_page(url=el.download_server)
        time.sleep(120)
        change_filename("server")
        # self.getDriver.open_page(url=el.download_unity)
        # time.sleep(4)
        # move_file("unity")


# if __name__ == '__main__':
#     suit = unittest.TestSuite()
#     case = TeslFlowDownload("test_case_download")
#     suit.addTest(case)
#     runner = unittest.TextTestRunner()
#     runner.run(suit)
