import requests
import time
from page.page_element import Test_language
from base.check_tools import absolute_path

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
    print(response.cookies)


def user():
    """

    """
    url = 'https://eu.phrase.com/idm-ui/api/v1/user'


def download(channel, url, cookie):
    """
    :return: 文件下载
    """
    if channel == 'server':
        date = 'attachment; filename="en.csv"; filename*=UTF-8''en.csv'
    else:
        date = 'attachment; filename="2024年09月06日 15点-04分language_android.xlsx"; filename*=UTF-8''2024年09月06日 15点-04分language_android.xlsx'
    headers = {
        'Content-Encoding': 'gzip',
        'authority': 'app.phrase.com',
        'method': 'GET',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-store',
        # 'accesstoken':'8wi7kBShUTeXdQHmN4rSARW7fdb7yCYID5tCUXmDpeUcJhSHg6aTkj4zIcUpzHgE',
        'Cookie': cookie,
        'Content-Disposition': date,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.'
                      '0 Safari/537.36 Edg/114.0.1823.43',
    }
    file_path = file_name(channel)
    download_request = requests.post(headers=headers, url=url, verify=False, stream=True)
    with open(file_path, "wb") as f:
        f.write(download_request.content)
    print(f"{channel}文件下载完成")


def language_download(channel, url, cookie, payload):
    """
    :return: 文件下载
    """
    url = url
    payload = payload
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f"{cookie}",
        'origin': 'https://app.phrase.com',
        'priority': 'u=0, i',
        'referer': 'https://app.phrase.com/accounts/starmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0/projects/starmaker-android/locales',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    file_path = file_name(channel)
    download_request = requests.post(headers=headers, url=url, verify=False, stream=True, data=payload)
    with open(file_path, "wb") as f:
        f.write(download_request.content)
    print(f"{channel}文件下载完成")


#
def file_name(channel):
    times = time.strftime('%Y年%m月%d日 %H点-%M分', time.localtime(time.time()))
    if channel == 'server':
        new_name = fr"{absolute_path('data')}\{channel}_data\{times}language_{channel}.csv"
        return new_name
    else:
        new_name = fr"{absolute_path('data')}\{channel}_data\{times}language_{channel}.xlsx"
        return new_name
