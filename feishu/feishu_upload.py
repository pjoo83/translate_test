import os
import requests
from page.feishu_data import Feishu_data
from feishu_get_token import get_tenant_access_token

fei = Feishu_data()


def upload_file(path, name, parent_node):
    """
    :param path: 文件本地地址
    :param name: 文件完整用户名
    :param parent_node: 上传指定文件夹的token
    :return: 返回文件上传信息
    """
    file_path = path
    file_size = os.path.getsize(file_path)
    url = fei.upload_url
    form = {
        'file_name': f'{name}',
        'parent_type': 'explorer',
        'parent_node': parent_node,
        'size': file_size,
    }
    files = [
        ('file', ('上传文件.xlsx', open(f'{file_path}', 'rb'), 'application/json'))
    ]
    token = 'Bearer ' + f"{get_tenant_access_token()}"
    headers = {'Authorization': token}

    response = requests.post(url=url, headers=headers, data=form, files=files)
    if response.json()['code'] == 0:
        print("文件已经上传", response.json())
        token = response.json()['data']['file_token']
        return token
    else:
        print("文件上传失败", response.json())
