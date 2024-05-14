import requests
import time
from page.page_element import Test_language

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


# login()
def download(channel, url):
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
        'Cookie': "_zitok=21a3db1bd27f06fe666f1688783650; OptanonAlertBoxClosed=2023-07-08T03:15:23.870Z; _pa_vid=1iahl6c-cv18-fhtjpd; uid=0945ddc4ee284f9401e5d94f866bf26e; _hjSessionUser_3270412=eyJpZCI6IjUzN2E1NDgyLTY4N2MtNTg5My1iYmY4LWRiNDE1N2IxNDIxZiIsImNyZWF0ZWQiOjE2ODg3ODYxMjQ2MzYsImV4aXN0aW5nIjp0cnVlfQ==; language=en; hubspotutk=567cf3f4d9a2b2275d482417a49fe121; intercom-id-qnzpmkdl=b8323223-293d-4c32-b7cf-5dfa46637777; intercom-device-id-qnzpmkdl=2be27183-ad2b-488a-9690-ab401bbfee8e; _pa_iid=ldm9min0; _fbp=fb.1.1709190673381.1977561661; _ga_KGJ9S35JX0=GS1.2.1709633514.5.1.1709633616.49.0.0; _gcl_au=1.1.158325581.1713953564; _ga=GA1.1.1186896170.1688786138; __hssrc=1; current_identity=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltWTNaRGsyTUdSbE5UVmpNVGszTjJFMk16UmxORGt5TXpkaE56UmpORFl6SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfaWRlbnRpdHkifX0%3D--a6efcbdbc5e6d1940ffd090f81fad56039b45000; current_account=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltTTVPRFF4TkRCallUQTBPVFl3TkRJek1tVXlZMlU1TTJJd01HUTJaV0U1SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfYWNjb3VudCJ9fQ%3D%3D--96da6ef4d0f1ca867607cf80c6be83b7c3081ee1; __hstc=24829477.567cf3f4d9a2b2275d482417a49fe121.1688786223073.1715661141537.1715667388156.14; _uetsid=7411953011a411efa65be7e1546d61de; _uetvid=b8a88450d6d111eeb9bfd53d6be3dd73; _ga_J2EQJSNGG3=GS1.1.1715666949.11.1.1715671380.0.0.0; mp_7ee5623b0363d19908a81c8e4e3a62a7_mixpanel=%7B%22distinct_id%22%3A%20%220945ddc4ee284f9401e5d94f866bf26e%22%2C%22%24device_id%22%3A%20%2218e0cb97295507-0054098581536e-1e525637-201b88-18e0cb97295507%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.phrase.com%2Faccounts%2Fstarmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0%2Fprojects%2Fstarmaker-server%2Flocales%22%2C%22%24initial_referring_domain%22%3A%20%22app.phrase.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%220945ddc4ee284f9401e5d94f866bf26e%22%2C%22Trial%22%3A%20false%2C%22Account%20Code%22%3A%20%22c984140ca049604232e2ce93b00d6ea9%22%2C%22Account%20Status%22%3A%20%22paying%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+14+2024+15%3A57%3A23+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202209.2.0&isIABGlobal=false&hosts=&consentId=4cb168b0-ec77-4209-943b-c9f3174539da&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CN%3BBJ&AwaitingReconsent=false; _phrase_session_sec=sVtUFtCBIRySXE5lPPb4KDCBoMTjfPoCbtfgal0XAPxlOZ35%2BSRQZbPUm0NtlZA0Gg2nMAyIV2ygYDTrzF3lOLvmEcSqt9cK6Bts73iLc6FQ7JH1eBqNGp9xK5EXso0J0mcXrN0TWagFd4fWqXBhZRQrKw4Eh5M1qB2Cl1W1SAuJVQ3nzX7PDHAc%2FtawPc%2Bk8adriAxW%2FS8srJj88deJ1dWaRlqqgWi2BZtq%2FNq1pcmNoaw8rW0uUkAVDbK89%2B2cB71HeA439XbXWRxtj%2FVtdWkC830arybf50EVqMNEGFDXcnya9Y14CODclmakgdYu34edlLw3ppVQg51S99LMw%2BRBcixdpsrh6spBaiLuGza%2FVTIvu2lvEOa5j0B210gB7XnBX8vv%2FZnQdSiMyGyAW3sGUHgMG%2FQDd69c1vid8IXURgzp5b0Y08t4jVf5Y3CSdWEadgHt0YZK%2Fqu6q30TqpSQ3bLseKRarlwF7LHdJR6vk2RNO%2FBPRhmbROtUUf1zF%2B%2BX1kXLoIoVh3ozImH9zQzoFgdvi3wmq%2BfoWqMEXpQu6LnXSkUBDhYCIs%2BS0rtI6m6l24fLDKu4yg7Uh8G2RAJ5J2LRxF1wjwhynyqcpAbTMaOsbU5%2BnFh85qnhRAD7V%2FIORjPN1YXCF6TuDj7wDe6xV0a%2BlRpN4jLs9il97B8SOg23camrggGvXyt8hI8I5b75N2cRURBypNEG7SwwRhASuYgTkOXzO79LwESwt72CYyquO0S8oBbHASVrPBDKJ9bSbCJ2%2FaaPVOxGm0k1qg3f8xDFPHxx5f2wmCM5PBsfzM87LPzkfaEUh4%2BtXaJzaKeynEO6OuOpkdK5uzEupuiAsm5JGVgqY0%2BXUsr%2FDotcMQZNlETHPbDV5P97hhd%2F95r1FzpkcMDqNu5OXQXSLTqsfBCiL1aVdFNebuPWFswW6yJYoWTozRFKcelC--7yLJ2Dyii7%2FxiSUn--04FCQh3rXx88PxDpXy%2FICg%3D%3D",
        # 'accesstoken':'8wi7kBShUTeXdQHmN4rSARW7fdb7yCYID5tCUXmDpeUcJhSHg6aTkj4zIcUpzHgE',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
    }
    file_path =file_name(channel)
    download_request = requests.get(headers=headers, url=url, verify=False, stream=True)
    with open(file_path, "wb") as f:
        f.write(download_request.content)
    print(f"{channel}文件下载完成")


def file_name(channel):
    times = time.strftime('%Y年%m月%d日 %H点-%M分', time.localtime(time.time()))
    if channel == 'server':
        new_name = f"../data/{channel}_data/{times}language_{channel}.csv"
        return new_name
    else:
        new_name = f"../data/{channel}_data/{times}language_{channel}.xlsx"
        return new_name
