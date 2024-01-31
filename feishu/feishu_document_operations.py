import json
from base.read_all_files import find_file
from feishu_get_token import get_tenant_access_token
import requests
from page.feishu_data import Feishu_data
from datetime import datetime
from feishu_upload import upload_file

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
        print("获取文件夹列表成功")

    return files.json()


def file_dic(filelist_url):
    """
    :return:获取文件夹清单后文件夹名称
    """
    filename_dic = {}
    files = get_files(filelist_url)["data"]["files"]
    for i in range(len(files)):
        token = files[i]["url"].split("/")[-1]
        filename_dic.update({files[i]["name"]: token})
    return filename_dic


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
        return response.json()['data']['url']
    else:
        print(f"创建失败------{response.json()}")


def get_file_dic():
    file_list = find_file('../result', 'xlsx')[:-3:-1]
    files_dic = {}
    for i in file_list:
        name = i.split('/')[-1]
        files_dic.update({name: i})
    return files_dic


def determine_existence():
    """
    :return: 判断年月文件是否存在
    """
    year_token = file_dic(fei.year_filelist_url)
    month_token = file_dic(fei.month_filelist_url)
    # year = f"{datetime.now().year}年"
    month = f"{datetime.now().month}月"
    year = '1994年'
    file_dict = get_file_dic()
    if year in year_token and month in month_token:
        print("文件夹已存在，不需要创建，请直接上传多语言文件")
        for k, v in file_dict.items():
            print(k, v)
            upload_file(path=v, name=k, parent_node=month_token[month])
    elif year in year_token and month not in month_token:
        month_token = create_folder(year_token[year], month).split("/")[-1]
        print(f"文件夹{month}已完成创建，将进行文件上传")
        for k, v in file_dict.items():
            upload_file(path=v, name=k, parent_node=month_token)
    else:
        year_token = create_folder(fei.translate_token, year).split("/")[-1]
        print(f"文件夹{year}已完成创建，将创建{month}文件夹")
        month_token = create_folder(year_token, month).split("/")[-1]
        print(f"文件夹{month}已完成创建，将进行文件上传")
        for k, v in file_dict.items():
            upload_file(path=v, name=k, parent_node=month_token)


if __name__ == '__main__':
    determine_existence()
