import requests
import time
import os
from datetime import datetime, timezone


# from base.check_tools import absolute_path


def ef_download(channel, ids):
    utc_midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    timestamp_ms = int(utc_midnight.timestamp() * 1000)
    url = 'https://ef-test.ushow.media/api-internal/phrase/translate/keys/tran/export?t=1742800404485&operator_id' \
          '=856&operator_name=hao.chang&operator_email=hao.chang@ushow.media&language=zh'
    payload = "{\"keys\":[],\"email\":\"hao.chang@ushow.media\"," \
              f"\"platform\":{ids},\"create_start_time\":1741910400000," \
              f"\"create_stop_time\":{timestamp_ms}}}"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'thinkjs=a3fe8a3b-6626-49ec-8dab-be9a512656fb; router_name=History; EF_USER_VERIFY=; '
                  'EF-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                  '.eyJ1c2VyX2lkIjozNjEsInRva2VuIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pF'
                  'M05ETXlNek00TmpJc0ltbHpjeUk2SW5OemJ5SXNJbTVpWmlJNk1UYzBNamd3TVRnMU55d2lkWE5sY2w5cFpDSTZPRFUyTENKdVl'
                  'XMWxJam9pYUdGdkxtTm9ZVzVuSWl3aVpXMWhhV3dpT2lKb1lXOHVZMmhoYm1kQWRYTm9iM2N1YldWa2FXRWlMQ0pzWVhKclgy'
                  'NWhiV1VpT2lMbHVMam10YWtpTENKc1lYSnJYMkYyWVhSaGNpSTZJbWgwZEhCek9pOHZjekV0YVcxbWFXeGxMbVpsYVhOb2RXT'
                  'mtiaTVqYjIwdmMzUmhkR2xqTFhKbGMyOTFjbU5sTDNZeEwzWXpYekF3YVRWZk5tTXdaV015WVRndE56TTNPQzAwTkRReUxUaz'
                  'FNMlV0TnpjMk9EQXdPVEJoWWpSbmZqOXBiV0ZuWlY5emFYcGxQVGN5ZURjeVhIVXdNREkyWTNWMFgzUjVjR1U5WEhVd01EST'
                  'JjWFZoYkdsMGVUMWNkVEF3TWpabWIzSnRZWFE5Y0c1blhIVXdNREkyYzNScFkydGxjbDltYjNKdFlYUTlMbmRsWW5BaUxDSn'
                  'NZWEpyWDJkeWIzVndJam9pYzNSaGNpSXNJbTVsWldSZmMyRm1aVjlqYUdWamF5STZabUZzYzJVc0lteHZaMmx1WDNScGJXVW'
                  'lPakUzTkRJNE1ERTROako5LkZPN0JtaDB0akh0WWktQ0pqT2dyanBVeHhYUmR6YlVyeVZNVVNUeElNeVEiLCJpYXQiOjE3ND'
                  'I4MDE4NjMsImV4cCI6MTc0Mjg4ODI2M30.TaoVOYw9l_udfeDrt2cBqbAF7Rea-ntn9XxeJg4vp_k; EF_USER_EMAIL=hao'
                  '.chang@ushow.media; EF_USER_NAME=hao.chang; sidebarStatus=0; thinkjs=d37bc577-d58e-4f7b-b878-d66'
                  '1fc3aece9',
        'operatorid': '361',
        'origin': 'https://ef-test.ushow.media',
        'priority': 'u=1, i',
        'referer': 'https://ef-test.ushow.media/translate/history',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/131.0.0.0 Safari/537.36'
    }
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
