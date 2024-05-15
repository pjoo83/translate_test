import requests
import time
from page.page_element import Test_language

A = Test_language()


def get_web_cookie():
    """
    :return: 返回浏览器的cookie
    """
    login_url = 'https://eu.phrase.com/idm-ui/signin'
    response = requests.get(login_url, verify=False)
    cookie = []
    for i in response.cookies:
        cookie.append(f'{i.name}={i.value}')
    return cookie


def login():
    """
    :return: 返回登陆的cookie
    """
    web_cookie = get_web_cookie()
    headers = {
        "authority": "eu.phrase.com",
        'method': 'POST',
        'path': '/idm-ui/api/v1/signin',
        'Accept': 'application/json',
        'scheme': 'https',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '54',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'Cookie': f'{web_cookie[0]},{web_cookie[1]}'

    }
    data = {'username': "translator.aa@ushow.media", 'password': "Re4@12345", 'rememberMe': False}
    url = 'https://eu.phrase.com/idm-ui/api/v1/signin'
    response = requests.post(url=url, json=data, headers=headers, verify=False)
    # return response.cookies
    print(response)


def download(channel, url, cookie):
    """
    :return: 文件下载
    """
    headers = {
        'authority': 'app.phrase.com',
        'method': 'GET',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'accesstoken':'8wi7kBShUTeXdQHmN4rSARW7fdb7yCYID5tCUXmDpeUcJhSHg6aTkj4zIcUpzHgE',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
    }
    file_path = file_name(channel)
    download_request = requests.get(headers=headers, url=url, verify=False, stream=True)
    with open(file_path, "wb") as f:
        f.write(download_request.content)
    print(f"{channel}文件下载完成")


def file_name(channel):
    times = time.strftime('%Y年%m月%d日 %H点-%M分', time.localtime(time.time()))
    if channel == 'server':
        new_name = fr"D:\project\starx_project\translate\data\{channel}_data\{times}language_{channel}.csv"
        return new_name
    else:
        new_name = fr"D:\project\starx_project\translate\data\{channel}_data\{times}language_{channel}.xlsx"
        return new_name