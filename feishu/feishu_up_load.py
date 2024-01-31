import os
import requests
from page.feishu_data import Feishu_data
from feishu_get_token import get_tenant_access_token

fei = Feishu_data()


def upload_file():
    file_path = '../result/2024年01月05日 17点-22分-37秒--android--language_test.xlsx'
    file_size = os.path.getsize(file_path)
    url = fei.upload_url
    form = {'file_name': '2024年01月05日 17点-22分-37秒--android--language_test.xlsx',
            'parent_type': 'explorer',
            'parent_node': 'TAqnf2ZshlHTPudf10vcuDX2nFh',
            'size': file_size,
            }
    files = [
        ('file', ('event_info(1).xlsx', open(f'{file_path}', 'rb'), 'application/json'))
    ]
    token = 'Bearer ' + f"{get_tenant_access_token()}"
    headers = {'Authorization': token}

    response = requests.post(url=url, headers=headers, data=form, files=files)
    if response.json()['code'] == 0:
        print("文件已经上传", response.json())
    else:
        print("文件上传失败", response.json())


if __name__ == '__main__':
    upload_file()
