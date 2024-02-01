from feishu_get_token import get_tenant_access_token
import requests
from page.feishu_data import Feishu_data
import json

fei = Feishu_data()


def get_chat_id():
    chat_id_url = fei.get_chats_id_url
    fei.content_type1['Authorization'] = "Bearer " + f"{get_tenant_access_token()}"
    headers = fei.content_type1
    response = requests.get(url=chat_id_url, headers=headers)
    print(response.json())


get_chat_id()


def send_msg():
    send_url = fei.send_msg_url
    fei.content_type1['Authorization'] = "Bearer " + f"{get_tenant_access_token()}"
    headers = fei.content_type1
    print(headers)
    data = json.dumps({
        "receive_id": "oc_2d069c00676d689335157645b92c2ecf",
        "msg_type": "text",
        "content": "{\"text\":\"测试测试\"}",
    })
    response = requests.post(url=send_url, headers=headers, data=data)
    print(response.json())
    return response.json()['data']['file_token']

# send_msg()
