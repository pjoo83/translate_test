import unittest
from base.testing import TestingCase
from base.check_tools import start_check
from base.read_all_files import find_file


class TeslFlowAndroid(TestingCase):

    def test_check(self):
        """
             安卓内容检查
        """
        self.getDriver.close_page()
        files = find_file(r"D:\project\translate\data\android_data", include_str="language_android", filter_strs=[".~"])
        for i in range(3):
            if len(files) > 1:

                start_check("android")
                break
            else:
                print("android_data文件中只有一个多语言文件，需要再下一份，保持文件夹中有两文件，就可以开始")


# if __name__ == '__main__':
#     suit = unittest.TestSuite()
#     case = TeslFlowAndroid("test_case_android")
#     suit.addTest(case)
#     runner = unittest.TextTestRunner()
#     runner.run(suit)
