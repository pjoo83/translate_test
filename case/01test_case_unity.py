import unittest
from base.read_all_files import find_file
from base.check_tools import start_check
from base.testing import TestingCase


class TeslFlowUnity(TestingCase):

    def test_check(self):
        """
            游戏端端内容检查
        """
        self.getDriver.close_page()
        files = find_file("../data/unity_data", include_str="language_unity", filter_strs=[".~"])
        if len(files) > 1:

            start_check("unity")
        else:
            print("unity_data文件中只有一个多语言文件，需要再下一份，保持文件夹中有两文件，就可以开始")


if __name__ == '__main__':
    suit = unittest.TestSuite()
    case = TeslFlowUnity("test_case_unity")
    suit.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suit)
