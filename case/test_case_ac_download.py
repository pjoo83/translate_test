import pytest
from page.page_element import Test_language
from base.interface_download import download

A = Test_language()


def test_download_flutter():
    """
        :return: flutter文件下载
    """
    # flutter下载
    download('flutter', A.download_flutter, A.download_common_cookie)


def test_download_android():
    """
    :return: 安卓文件下载
    """
    download('android', A.download_android, A.download_common_cookie)


def test_download_ios():
    """
    :return: ios文件下载
    """
    download('ios', A.download_ios, A.download_common_cookie)
    # server下载


def test_download_server():
    """
    :return: 服务文件下载
    """
    download('server', A.download_server, A.download_common_cookie)


if __name__ == '__main__':
    pytest.main()
