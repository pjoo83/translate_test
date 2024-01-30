from page.feishu_data import Feishu_data
import requests
import json

fei = Feishu_data()


def get_tenant_access_token():
    """
    :return: 自建应用获取tenant_access_token
    """
    body = fei.req_token_body
    headers = fei.content_type
    request = requests.post(url=fei.tenant_access_url_token, json=body, headers=headers)
    tenant_token = request.json()['tenant_access_token']
    return tenant_token


def get_app_access_token():
    """
    :return: 获取自建应用app_access_token
    """
    headers = fei.content_type
    body = fei.req_token_body
    response = requests.post(url=fei.app_access_token_url, json=body, headers=headers)
    app_access_token = response.json()['app_access_token']
    return app_access_token


def get_user_access_token():
    """
    :return: 获取网页应用token
    """
    fei.content_type1['Authorization'] = "Bearer " + f"{get_app_access_token()}"
    headers = fei.content_type1
    payload = json.dumps({
        "code": "xMSldislSkdK",
        "grant_type": "authorization_code"
    })
    response = requests.post(url=fei.user_access_token, headers=headers, data=payload)
    body = response.text


# get_user_access_token()


