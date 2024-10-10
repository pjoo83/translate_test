from page.page_element import Test_language
from base.interface_download import language_download
from base.check_tools import del_file

A = Test_language()


def test_download_flutter():
    """
        :return: flutter文件下载
    """
    del_file()
    if language_download('flutter', A.download_flutter, A.download_common_cookie, A.flutter_payload):
        print("flutter文件已完成下载")


def test_download_android():
    """
    :return: 安卓文件下载
     """
    if language_download('android', A.download_android, A.download_common_cookie, A.android_payload):
        print("android文件已完成下载")


def test_download_ios():
    """
    :return: ios文件下载
    """
    if language_download('ios', A.download_ios, A.download_common_cookie, A.ios_payload):
        print("ios文件已完成下载")


def test_download_server():
    """
    :return: 服务端文件下载
    """
    if language_download('server', A.download_server, A.download_common_cookie, A.server_payload):
        print("server文件下载完成")


def test_download_cocos():
    """
    :return: cocos文件下载
    """
    if language_download('cocos', A.download_cocos, A.download_common_cookie, A.cocos_payload):
        print("cocos文件已完成下载")
