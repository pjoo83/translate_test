import json

import requests
import time
from datetime import datetime, timezone, timedelta


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
        'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        'Cookie': '_ga=GA1.1.1792866753.1713751715; _ga_Y5QLWEHNZ4=GS2.1.s1759063930$o111$g1$t1759064843$j60$l0$h0; thinkjs=4f9615dd-2133-459e-a64b-22bbcb43a361; EF_USER_VERIFY=; EF_USER_EMAIL=hao.chang@ushow.media; EF_USER_NAME=hao.chang; router_name=History; EF-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5OTQsInRva2VuIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFM05qQTBNVEE1TXpVc0ltbHpjeUk2SW5OemJ5SXNJbTVpWmlJNk1UYzFPVGszT0Rrek1Dd2lkWE5sY2w5cFpDSTZNVEUwTkN3aWJtRnRaU0k2SW1oaGJ5NWphR0Z1WnlJc0ltVnRZV2xzSWpvaWFHRnZMbU5vWVc1blFIVnphRzkzTG0xbFpHbGhJaXdpYkdGeWExOXVZVzFsSWpvaTViaTQ1cldwSWl3aWJHRnlhMTloZG1GMFlYSWlPaUpvZEhSd2N6b3ZMM014TFdsdFptbHNaUzVtWldsemFIVmpaRzR1WTI5dEwzTjBZWFJwWXkxeVpYTnZkWEpqWlM5Mk1TOTJNMTh3TUc4eFgyTmhOek0yTm1VMExUWTROek10TkdabE5pMWhNRE00TFRoaU5UTTNNV1F3T0dNMlozNF9hVzFoWjJWZmMybDZaVDAzTW5nM01seDFNREF5Tm1OMWRGOTBlWEJsUFZ4MU1EQXlObkYxWVd4cGRIazlYSFV3TURJMlptOXliV0YwUFhCdVoxeDFNREF5Tm5OMGFXTnJaWEpmWm05eWJXRjBQUzUzWldKd0lpd2liR0Z5YTE5bmNtOTFjQ0k2SW5OMFlYSWlMQ0p1WldWa1gzTmhabVZmWTJobFkyc2lPbVpoYkhObExDSnNiMmRwYmw5MGFXMWxJam94TnpVNU9UYzRPVEkzZlEubDZsaEhpdHVJQXVlWldyR05CNnJqLTJnTThGZV9CNmhCY1paZzlPOFcxQSIsImlhdCI6MTc2MDA4MDc2NywiZXhwIjoxNzYwMTY3MTY3fQ.I7SQrY33_ms3SprSqxJuX3C41I8cvJJ81P2TTvCDH8Q; sidebarStatus=0'
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
        print(download_request.json())
        file_url = download_request.json()['data']

        response = requests.request("get", file_url, headers=headers, data=payload)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"{channel}文件下载完成")
        # # response = requests.request("POST", url, headers=headers, data=payload)
        # file_path = file_name(channel)
        # download_request = requests.post(headers=headers, url=url, verify=False, stream=True, data=payload)
        # file_url = download_request.json()['data']
        # response = requests.request("get", file_url, headers=headers, data=payload)
        # with open(file_path, "wb") as f:
        #     f.write(response.content)
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


# if __name__ == '__main__':
#     ef_download('server', [
#         "The Voice UK Playlist",
#         "All",
#         'Group'])
