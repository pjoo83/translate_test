from base.ef_download import ef_download
from base.check_tools import del_file


def test_download_flutter():
    """
        :return: flutter文件下载
    """
    del_file()
    if ef_download('flutter', 3):
        print("flutter文件已完成下载")


def test_download_android():
    """
    :return: 安卓文件下载
     """
    if ef_download('android', 1):
        print("android文件已完成下载")


def test_download_ios():
    """
    :return: ios文件下载
    """
    if ef_download('ios', 2):
        print("android文件已完成下载")


def test_download_server():
    """
    :return: 服务端文件下载
    """
    if ef_download('server', 3):
        print("server文件下载完成")


def test_download_cocos():
    """
    :return: cocos文件下载
    """
    if ef_download('cocos', 7):
        print("cocos文件已完成下载")
