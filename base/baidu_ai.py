import requests
import json

API_KEY = "8UDgNe4j4ymztfXZZV8EsQ86"
SECRET_KEY = "FQ1hV8v3gs7znZGPdiVv3PA7sHLKbCyH"


def main(test):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/yi_34b_chat?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": f"{test}每句中“翻译：”后面的语句的意思相近吗，只用告诉我是不是相近，如果不相近的话，第几个不相近"
            },
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.json()['result'])
    return response.json()['result']


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main("你是谁")
