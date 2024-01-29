class Feishu_data:
    def __init__(self):
        # 获取自建应用
        self.req_token_body = {
            "app_id": "cli_a53891a386b0d00c",
            "app_secret": "3GLTo0F66pbjveu8zfe36dZ0HFBFma64"
        }
        # 自建应用的url
        self.app_access_token_url = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal'

        self.user_access_token = 'https://open.feishu.cn/open-apis/authen/v1/oidc/access_token'
        self.tenant_access_url_token = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        self.content_type = {"Content-Type": "application/json; charset=utf-8"}
        self.content_type1 = {
            "Content-Type": "application/json;charset=utf-8",
            'Authorization': ""
        }
        self.req_files_url = "https://open.feishu.cn/open-apis/drive/v1/files?direction=DESC&order_by=EditedTime"

        # 文件上传
        self.upload_url = 'https://open.feishu.cn/open-apis/drive/v1/files/upload_all'
