import requests
import time
from datetime import datetime, timezone, timedelta
import json


def ef_download(channel, ids):
    utc_midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = utc_midnight + timedelta(days=1)
    timestamp_ms = int(tomorrow.timestamp() * 1000)
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
        'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        'Cookie': '_ga=GA1.1.561799247.1757300306; _ga_Y5QLWEHNZ4=GS2.1.s1757300305^$o1^$g1^$t1757301126^$j60^$l0^$h0; thinkjs=6aebd188-03ff-4910-b674-d7dab2c1ed42; router_name=History; EF_USER_VERIFY=; EF-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5OTQsInRva2VuIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFM05Ua3hPVGMxTXpVc0ltbHpjeUk2SW5OemJ5SXNJbTVpWmlJNk1UYzFPRGMyTlRVek1Dd2lkWE5sY2w5cFpDSTZNVEUwTkN3aWJtRnRaU0k2SW1oaGJ5NWphR0Z1WnlJc0ltVnRZV2xzSWpvaWFHRnZMbU5vWVc1blFIVnphRzkzTG0xbFpHbGhJaXdpYkdGeWExOXVZVzFsSWpvaTViaTQ1cldwSWl3aWJHRnlhMTloZG1GMFlYSWlPaUpvZEhSd2N6b3ZMM014TFdsdFptbHNaUzVtWldsemFIVmpaRzR1WTI5dEwzTjBZWFJwWXkxeVpYTnZkWEpqWlM5Mk1TOTJNMTh3TUc4eFgyTmhOek0yTm1VMExUWTROek10TkdabE5pMWhNRE00TFRoaU5UTTNNV1F3T0dNMlozNF9hVzFoWjJWZmMybDZaVDAzTW5nM01seDFNREF5Tm1OMWRGOTBlWEJsUFZ4MU1EQXlObkYxWVd4cGRIazlYSFV3TURJMlptOXliV0YwUFhCdVoxeDFNREF5Tm5OMGFXTnJaWEpmWm05eWJXRjBQUzUzWldKd0lpd2liR0Z5YTE5bmNtOTFjQ0k2SW5OMFlYSWlMQ0p1WldWa1gzTmhabVZmWTJobFkyc2lPbVpoYkhObExDSnNiMmRwYmw5MGFXMWxJam94TnpVNE56WTFOVEkzZlEuOTlHVHNEYWdqUGZJcHE4UlVfVUFOakZ2SW04NUd4b0J5ZXF4VXZrajh1YyIsImlhdCI6MTc1ODc2NTUzOCwiZXhwIjoxNzU4ODUxOTM4fQ.HjSq3sH6SYJTLe-DoTSRRADja19C8SR2OJOc7uLPgyQ; EF_USER_EMAIL=hao.chang^@ushow.media; EF_USER_NAME=hao.chang; sidebarStatus=0'
    }
    if channel == 'server':
        keys = ids
        payload_dict = {
            "keys": keys,
            "email": "hao.chang@ushow.media",
            "platform": 0
        }
        payload = json.dumps(payload_dict)
        download_request = requests.request("POST", url, headers=headers, data=payload)
        file_path = file_name(channel)
        file_url = download_request.json()['data']
        response = requests.request("get", file_url, headers=headers, data=payload)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"{channel}文件下载完成")
    else:
        payload = build_payload(ids, timestamp_ms)
        file_path = file_name(channel)
        download_request = requests.post(headers=headers, url=url, verify=False, stream=True, data=payload)
        file_url = download_request.json()['data']
        print(f"下载链接: {file_url}")
        response = requests.request("get", file_url, stream=True, headers=headers)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"{channel}文件下载完成")


def file_name(channel):
    times = time.strftime('%Y年%m月%d日 %H点-%M分', time.localtime(time.time()))
    new_name = fr'D:\project\starx_project\translate\data\{channel}_data\{times}language_{channel}.xlsx'
    return new_name


def build_payload(platform, create_stop_time):
    """
    return: 返回payload
    """
    payload_dict = {
        "keys": [],
        "email": "hao.chang@ushow.media",
        "platform": platform,
        "create_start_time": 1741910400000,
        "create_stop_time": create_stop_time
    }
    return json.dumps(payload_dict)


if __name__ == '__main__':
    ef_download('android', 1)
