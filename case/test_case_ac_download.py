from page.page_element import Test_language
from base.interface_download import download
from base.check_tools import  del_file
A = Test_language()


def test_download_flutter():
    """
        :return: flutter文件下载
    """
    del_file()
    if download('flutter', A.download_flutter, A.download_common_cookie):
        print("flutter文件已完成下载")


def test_download_android():
    """
    :return: 安卓文件下载
     """
    if download('android', A.download_android, A.download_common_cookie):
        print("android文件已完成下载")


def test_download_ios():
    """
    :return: ios文件下载
    """
    if download('ios', A.download_ios, A.download_common_cookie):
        print("ios文件已完成下载")


def test_download_server():
    """
    :return: 服务端文件下载
    """
    if download('server', A.download_server, A.download_common_cookie):
        print("server文件已完成下载")
