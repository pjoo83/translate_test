import requests
import time
from datetime import datetime, timezone, timedelta
from database_tools import execute_sql


def ef_download(channel, ids):
    utc_midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    timestamp_ms = int(utc_midnight.timestamp() * 1000)
    url = "https://ef.ushow.media/api-internal/phrase/translate/keys/tran/export?t=1744010316350&operator_id=994&o" \
          "perator_name=hao.chang&operator_email=hao.chang@ushow.media&language=zh"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'operatorid': '994',
        'origin': 'https://ef.ushow.media',
        'priority': 'u=1, i',
        'referer': 'https://ef.ushow.media/translate/history',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Cookie': '_ga_Y5QLWEHNZ4=GS1.1.1736474542.33.0.1736474542.60.0.0; _ga=GA1.2.1792866'
                  '753.1713751715; thinkjs=3703e188-b933-499b-b241-973e8ab90555; router_name=Hi'
                  'story; EF_USER_VERIFY=; EF-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2'
                  'VyX2lkIjo5OTQsInRva2VuIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5Lm'
                  'V5SmxlSEFpT2pFM05EUTBNakk0TVRFc0ltbHpjeUk2SW5OemJ5SXNJbTVpWmlJNk1UYzBNems1TU'
                  'Rnd05pd2lkWE5sY2w5cFpDSTZNVEUwTkN3aWJtRnRaU0k2SW1oaGJ5NWphR0Z1WnlJc0ltVnRZV'
                  '2xzSWpvaWFHRnZMbU5vWVc1blFIVnphRzkzTG0xbFpHbGhJaXdpYkdGeWExOXVZVzFsSWpvaTVi'
                  'aTQ1cldwSWl3aWJHRnlhMTloZG1GMFlYSWlPaUpvZEhSd2N6b3ZMM014TFdsdFptbHNaUzVtWlds'
                  'emFIVmpaRzR1WTI5dEwzTjBZWFJwWXkxeVpYTnZkWEpqWlM5Mk1TOTJNMTh3TUdrMVh6WmpNR1Zq'
                  'TW1FNExUY3pOemd0TkRRME1pMDVOVE5sTFRjM05qZ3dNRGt3WVdJMFozNF9hVzFoWjJWZmMybDZa'
                  'VDAzTW5nM01seDFNREF5Tm1OMWRGOTBlWEJsUFZ4MU1EQXlObkYxWVd4cGRIazlYSFV3TURJMlptO'
                  'XliV0YwUFhCdVoxeDFNREF5Tm5OMGFXTnJaWEpmWm05eWJXRjBQUzUzWldKd0lpd2liR0Z5YTE5bm'
                  'NtOTFjQ0k2SW5OMFlYSWlMQ0p1WldWa1gzTmhabVZmWTJobFkyc2lPbVpoYkhObExDSnNiMmRwYm'
                  'w5MGFXMWxJam94TnpRek9Ua3dOems0ZlEuR1pncnJYLU9IOVVDZ2dnenVTUjZrUzNwMWNaQ0oxUFB'
                  'leWdIZjlfYkprbyIsImlhdCI6MTc0NDAxMDI5OSwiZXhwIjoxNzQ0MDk2Njk5fQ.T_XN9UH4jT4l-'
                  'ZVLV82Dy_YoTbZKS6LgwkG8X82nsYk; EF_USER_EMAIL=hao.chang@ushow.media; EF_USER_'
                  'NAME=hao.chang; sidebarStatus=0'
    }
    if channel =='server':
        payload = "{\"keys\":[],\"email\":\"hao.chang@ushow.media\"," \
                  f"\"platform\":{ids},\"create_start_time\":{execute_sql(0, 0, 0, 0, 'query')}," \
                  f"\"create_stop_time\":{timestamp_ms}}}"
        # response = requests.request("POST", url, headers=headers, data=payload)
        file_path = file_name(channel)
        download_request = requests.post(headers=headers, url=url, verify=False, stream=True, data=payload)
        file_url = download_request.json()['data']
        response = requests.request("get", file_url, headers=headers, data=payload)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"{channel}文件下载完成")
    else:
        payload = "{\"keys\":[],\"email\":\"hao.chang@ushow.media\"," \
                  f"\"platform\":{ids},\"create_start_time\":1741910400000," \
                  f"\"create_stop_time\":{timestamp_ms}}}"
        # response = requests.request("POST", url, headers=headers, data=payload)
        file_path = file_name(channel)
        download_request = requests.post(headers=headers, url=url, verify=False, stream=True, data=payload)
        file_url = download_request.json()['data']
        response = requests.request("get", file_url, headers=headers, data=payload)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"{channel}文件下载完成")


def file_name(channel):
    times = time.strftime('%Y年%m月%d日 %H点-%M分', time.localtime(time.time()))
    new_name = f'/Users/lbj/Desktop/starx/project/translate_test/data/{channel}_data/{times}language_{channel}.xlsx'
    return new_name


if __name__ == '__main__':
    ef_download('ios', 2)
