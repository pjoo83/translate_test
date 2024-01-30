import os
import requests
from requests_toolbelt import MultipartEncoder
from page.feishu_data import Feishu_data
from feishu_get_token import get_tenant_access_token

fei = Feishu_data()


def upload_file():
    file_path = "../data/ios_data/2024年01月05日 17点-22分-27秒language_ios.xlsx"
    file_size = os.path.getsize(file_path)
    url = fei.upload_url
    form = {'file_name': '2024年01月05日 17点-22分-27秒language_ios',
            'parent_type': 'explorer',
            'parent_node': 'EHQvfnHFOl0yJhdcYHUcZAKDnhA',
            'size': str(file_size),
            'file': (open(file_path, 'rb'))}
    multi_form = MultipartEncoder(form)
    token = 'Bearer ' + f"{get_tenant_access_token()}"
    headers = {'Content-Type': token,
               "boundary": ""}
    response = requests.request("POST", url, headers=headers, data=multi_form)
    print(response.text)


if __name__ == '__main__':
    upload_file()
