from feishu_get_token import get_tenant_access_token
import requests
from page.feishu_data import Feishu_data

fei = Feishu_data()


def get_files():
    """
    :return: 获取总文件夹下清单
    """
    headers = {
        'Authorization': 'Bearer t-g1041ue1KYV5FDUG24JRNLLRFHBYLXOJRBG6OL5B'
    }
    payload = ''
    files = requests.get(url=fei.files_list_url, headers=headers, data=payload)
    if files.json()["code"] != 0:
        print(f"获取文件列表错误错误信息如下{files.json()}", )
    else:
        print("获取列表成功")
        return files.json()



def file_list():
    file_lists = []
    for file in get_files():
        psss

