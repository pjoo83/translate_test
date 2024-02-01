from base.read_all_files import find_file
from feishu_get_token import get_tenant_access_token
from page.feishu_data import Feishu_data
from datetime import datetime
from feishu_upload import upload_file
import requests
import json
from feishu_send_message import start_send

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
        token = files[i]["token"]
        filename_dic.update({files[i]["name"]: token})
    print(filename_dic)
    return filename_dic


def create_folder(token, name):
    """
    :return: 创建文件夹
    """
    payload = json.dumps(
        {
            "folder_token": f"{token}",
            "name": f"{name}"
        })
    fei.content_type1["Authorization"] = f'Bearer {get_tenant_access_token()}'
    headers = fei.content_type1
    response = requests.post(url=fei.create_folder_url, headers=headers, data=payload)
    if response.json()["code"] == 0:
        print(f"创建成功------{response.json()}")
        return response.json()['data']['token']
    else:
        print(f"创建失败------{response.json()}")


def get_file_dic():
    """
    :return: 将文件与绝对路径组成字典
    """
    file_list = find_file('../result', 'xlsx')[:-3:-1]
    files_dic = {}
    for i in file_list:
        name = i.split('/')[-1]
        files_dic.update({name: i})
    return files_dic


def check_folder():
    """
    :return: 判断是否存在，不存在则调用创建
    """
    year_list = file_dic(fei.year_filelist_url)
    month_list = file_dic(fei.month_filelist_url)
    year = f"{datetime.now().year}年"
    month = f"{datetime.now().month}月"
    if year in year_list and month in month_list:
        print("文件夹已存在，不需要创建，将直接上传多语言文件")
        upload_all(parent_node=month_list[month])
    elif year in year_list and month not in month_list:
        month_token = create_folder(year_list[year], month)
        print(f"文件夹{month}已完成创建，将进行文件上传")
        upload_all(parent_node=month_token)
    else:
        year_token = create_folder(fei.translate_token, year)
        print(f"文件夹{year}已完成创建，将创建{month}文件夹")
        month_token = create_folder(year_token, month)
        print(f"文件夹{month}已完成创建，将进行文件上传")
        upload_all(parent_node=month_token)


def upload_all(parent_node):
    """
    :param parent_node:文件上传的指定文件夹token
    :return:
    """
    file_dict = get_file_dic()
    for k, v in file_dict.items():
        token = upload_file(path=v, name=k, parent_node=parent_node)
        token = upload_file_url(token)
        start_send(token)


def upload_file_url(token):
    """
    :param token: 上传文件获取的token
    :return: 返回拼接后url
    """
    file_url = fei.file_url + f"{token}"
    return file_url


if __name__ == '__main__':
    check_folder()
