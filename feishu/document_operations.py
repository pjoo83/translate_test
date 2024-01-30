import json

from feishu_get_token import get_tenant_access_token
import requests
from page.feishu_data import Feishu_data
from datetime import datetime

fei = Feishu_data()


def get_files(filelist_url):
    """
    :return: 获取总文件夹下清单
    """
    headers = {
        'Authorization': f'Bearer {get_tenant_access_token()}'
    }
    payload = ''
    files = requests.get(url=filelist_url, headers=headers, data=payload)
    if files.json()["code"] != 0:
        print(f"获取文件列表错误错误信息如下{files.json()}", )
    else:
        print("获取列表成功")
        return files.json()


def file_list(filelist_url):
    """
    :return:获取文件夹清单后文件夹名称
    """
    filename_dic = {}
    files = get_files(filelist_url)["data"]["files"]
    for i in range(len(files)):
        token=files[i]["url"].split("/")[-1]
        filename_dic.update({files[i]["name"]: token})
    return filename_dic


file_list(fei.year_filelist_url)


def determine_existence():
    """
    :return: 判断年月文件是否存在
    """
    year_list = file_list(fei.year_filelist_url)
    month_list = file_list(fei.month_filelist_url)
    year = f"{datetime.now().year}年"
    month = f"{datetime.now().month}月"
    if year in year_list:
        if month in month_list:
            print("文件夹已存在，不需要创建，请直接上传多语言文件")
        else:

            pass
    else:
        create_folder(fei.translate_token, year)


def create_folder(token, name):
    """
    :return: 创建文件夹
    """
    payload = json.dumps({
        "folder_token": f"{token}",
        "name": f"{name}"
    })
    fei.content_type1["Authorization"] = f'Bearer {get_tenant_access_token()}'
    headers = fei.content_type1
    response = requests.post(url=fei.create_folder_url, headers=headers, data=payload)
    if response.json()["code"] == 0:
        print(f"创建成功------{response.json()}")
    else:
        print(f"创建失败------{response.json()}")