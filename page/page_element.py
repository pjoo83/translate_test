from selenium.webdriver.common.by import By


class Test_language:
    def __init__(self):
        self.login_url = "https://eu.phrase.com/idm-ui/signin"
        # 姓名
        self.uname = (By.NAME, "username")
        # 密码
        self.pwd = (By.NAME, "password")
        # 登录
        self.login = (By.XPATH, "//button[1]")
        # 关闭cookies弹窗
        self.close_cookie = (By.XPATH, "//button[contains(.,'Accept all cookies')]")
        # 进入翻译平台
        self.open = (By.XPATH, "//a[contains(.,'Open')]")
        # 选择安卓
        self.android = (By.XPATH, "//a[contains(.,'StarMaker-Android')]")
        # 选择翻译
        self.language = (By.XPATH, "//a[contains(.,'Language')]")
        # 全选框
        self.all = (By.XPATH, "//input[@id='']")
        # 选择下载
        self.export = (By.XPATH, "//button[@id='export-locales-btn']")
        # 请求安卓多语言下载
        self.download_android = "http://app.phrase.com/accounts/starmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0" \
                                "/projects/starmaker-android/locales/download?utf8=%E2%9C%93&locale_names%5B%5D=en" \
                                "&locale_names%5B%5D=ar&locale_names%5B%5D=bn&locale_names%5B%5D=cs&locale_names%5B" \
                                "%5D=de&locale_names%5B%5D=es&locale_names%5B%5D=fr&locale_names%5B%5D=in" \
                                "&locale_names%5B%5D=it&locale_names%5B%5D=ja&locale_names%5B%5D=ko&locale_names%5B" \
                                "%5D=ms&locale_names%5B%5D=pt-rBR&locale_names%5B%5D=ru&locale_names%5B%5D=ru-rRU" \
                                "&locale_names%5B%5D=sr&locale_names%5B%5D=th&locale_names%5B%5D=tr&locale_names%5B" \
                                "%5D=tr-rTR&locale_names%5B%5D=ur-rPK&locale_names%5B%5D=vi&locale_names%5B%5D=zh-rCN" \
                                "&locale_names%5B%5D=zh-rTW&locale_download%5Bfile_format%5D=xlsx&locale_download" \
                                "%5Bformat_options%5D%5Bdocument_id%5D=&locale_download%5Bformat_options%5D" \
                                "%5Binclude_headers%5D=0&locale_download%5Bformat_options%5D%5Binclude_headers%5D=1" \
                                "&locale_download%5Bformat_options%5D%5Bexport_tags%5D=0&locale_download" \
                                "%5Bformat_options%5D%5Bexport_system_tags%5D=0&locale_download%5Bformat_options%5D" \
                                "%5Bexport_max_characters_allowed%5D=0&locale_download%5Binclude_empty_translations" \
                                "%5D=0&locale_download%5Binclude_translated_keys%5D=0&locale_download" \
                                "%5Bexclude_empty_zero_forms%5D=0&locale_download%5Binclude_unverified_translations" \
                                "%5D=0&locale_download%5Binclude_unverified_translations%5D=1&locale_download" \
                                "%5Buse_last_reviewed_version%5D=0&locale_download%5Btags%5D%5B%5D=&locale_download" \
                                "%5Bkeep_notranslate_tags%5D=0&locale_download%5Brenders_default_locale%5D=0" \
                                "&locale_download%5Bencoding%5D=UTF-8 "
        # 请求IOS多语言文件
        self.download_ios = "http://app.phrase.com/accounts/starmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0/projects" \
                            "/starmaker-ios/locales/download?utf8=%E2%9C%93&locale_names%5B%5D=en&locale_names%5B%5D" \
                            "=ar&locale_names%5B%5D=bn-IN&locale_names%5B%5D=de&locale_names%5B%5D=es&locale_names%5B" \
                            "%5D=fr&locale_names%5B%5D=id&locale_names%5B%5D=it&locale_names%5B%5D=ja&locale_names%5B" \
                            "%5D=ko&locale_names%5B%5D=ms&locale_names%5B%5D=pt-BR&locale_names%5B%5D=ru-RU" \
                            "&locale_names%5B%5D=th&locale_names%5B%5D=tr-TR&locale_names%5B%5D=vi&locale_names%5B%5D" \
                            "=zh-CN&locale_names%5B%5D=zh-Hant&locale_download%5Bfile_format%5D=xlsx&locale_download" \
                            "%5Bformat_options%5D%5Bdocument_id%5D=&locale_download%5Bformat_options%5D" \
                            "%5Binclude_headers%5D=0&locale_download%5Bformat_options%5D%5Binclude_headers%5D=1" \
                            "&locale_download%5Bformat_options%5D%5Bexport_tags%5D=0&locale_download%5Bformat_options" \
                            "%5D%5Bexport_system_tags%5D=0&locale_download%5Bformat_options%5D" \
                            "%5Bexport_max_characters_allowed%5D=0&locale_download%5Binclude_empty_translations%5D=0" \
                            "&locale_download%5Binclude_translated_keys%5D=0&locale_download" \
                            "%5Bexclude_empty_zero_forms%5D=0&locale_download%5Binclude_unverified_translations%5D=0" \
                            "&locale_download%5Binclude_unverified_translations%5D=1&locale_download" \
                            "%5Buse_last_reviewed_version%5D=0&locale_download%5Btags%5D%5B%5D=&locale_download" \
                            "%5Bkeep_notranslate_tags%5D=0&locale_download%5Brenders_default_locale%5D=0" \
                            "&locale_download%5Bencoding%5D=UTF-8 "

        # 请求服务端多语言
        self.download_server = "https://app.phrase.com/accounts/starmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0" \
                               "/projects/starmaker-server/locales/download?utf8=%E2%9C%93&locale_names%5B%5D=en" \
                               "&locale_names%5B%5D=af&locale_names%5B%5D=ar&locale_names%5B%5D=ar-SA&locale_names%5B" \
                               "%5D=bn-IN&locale_names%5B%5D=cz&locale_names%5B%5D=da&locale_names%5B%5D=de" \
                               "&locale_names%5B%5D=en-IN&locale_names%5B%5D=es&locale_names%5B%5D=es-MX&locale_names" \
                               "%5B%5D=fr&locale_names%5B%5D=hi&locale_names%5B%5D=hi-IN&locale_names%5B%5D=in" \
                               "&locale_names%5B%5D=it&locale_names%5B%5D=ja&locale_names%5B%5D=kn-IN&locale_names%5B" \
                               "%5D=ko&locale_names%5B%5D=ml-IN&locale_names%5B%5D=ms&locale_names%5B%5D=my" \
                               "&locale_names%5B%5D=pa-PK&locale_names%5B%5D=pt-BR&locale_names%5B%5D=ru&locale_names" \
                               "%5B%5D=sr&locale_names%5B%5D=sv&locale_names%5B%5D=sw&locale_names%5B%5D=ta-IN" \
                               "&locale_names%5B%5D=te-IN&locale_names%5B%5D=th&locale_names%5B%5D=tl&locale_names%5B" \
                               "%5D=tr&locale_names%5B%5D=ur-PK&locale_names%5B%5D=vi&locale_names%5B%5D=zh-CN" \
                               "&locale_names%5B%5D=zh-TW&locale_download%5Bfile_format%5D=csv&locale_download" \
                               "%5Bformat_options%5D%5Bdocument_id%5D=&locale_download%5Bformat_options%5D" \
                               "%5Binclude_headers%5D=0&locale_download%5Bformat_options%5D%5Binclude_headers%5D=1" \
                               "&locale_download%5Bformat_options%5D%5Bexport_tags%5D=0&locale_download" \
                               "%5Bformat_options%5D%5Bexport_system_tags%5D=0&locale_download%5Bformat_options%5D" \
                               "%5Bexport_max_characters_allowed%5D=0&locale_download%5Binclude_empty_translations%5D" \
                               "=0&locale_download%5Binclude_translated_keys%5D=0&locale_download" \
                               "%5Bexclude_empty_zero_forms%5D=0&locale_download%5Binclude_unverified_translations%5D" \
                               "=0&locale_download%5Binclude_unverified_translations%5D=1&locale_download" \
                               "%5Buse_last_reviewed_version%5D=0&locale_download%5Btags%5D%5B%5D=&locale_download" \
                               "%5Bkeep_notranslate_tags%5D=0&locale_download%5Bencoding%5D=UTF-8"

        # 请求unity
        self.download_unity = "https://app.phrase.com/accounts/starmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0" \
                              "/projects/starmaker-unity/locales/download?utf8=%E2%9C%93&locale_names%5B%5D=en" \
                              "&locale_names%5B%5D=ar&locale_names%5B%5D=bn-IN&locale_names%5B%5D=cs&locale_names%5B" \
                              "%5D=de&locale_names%5B%5D=es&locale_names%5B%5D=fr&locale_names%5B%5D=in&locale_names" \
                              "%5B%5D=it&locale_names%5B%5D=ja&locale_names%5B%5D=ko&locale_names%5B%5D=ms" \
                              "&locale_names%5B%5D=pt-BR&locale_names%5B%5D=ru-RU&locale_names%5B%5D=sr&locale_names" \
                              "%5B%5D=th&locale_names%5B%5D=tr-TR&locale_names%5B%5D=ur-PK&locale_names%5B%5D=vi" \
                              "&locale_names%5B%5D=zh&locale_names%5B%5D=zh-TW&locale_download%5Bfile_format%5D=xlsx" \
                              "&locale_download%5Bformat_options%5D%5Bdocument_id%5D=&locale_download" \
                              "%5Bformat_options%5D%5Binclude_headers%5D=0&locale_download%5Bformat_options%5D" \
                              "%5Binclude_headers%5D=1&locale_download%5Bformat_options%5D%5Bexport_tags%5D=0" \
                              "&locale_download%5Bformat_options%5D%5Bexport_system_tags%5D=0&locale_download" \
                              "%5Bformat_options%5D%5Bexport_max_characters_allowed%5D=0&locale_download" \
                              "%5Binclude_empty_translations%5D=0&locale_download%5Binclude_translated_keys%5D=0" \
                              "&locale_download%5Bexclude_empty_zero_forms%5D=0&locale_download" \
                              "%5Binclude_unverified_translations%5D=0&locale_download" \
                              "%5Binclude_unverified_translations%5D=1&locale_download%5Buse_last_reviewed_version%5D" \
                              "=0&locale_download%5Btags%5D%5B%5D=&locale_download%5Bkeep_notranslate_tags%5D=0" \
                              "&locale_download%5Brenders_default_locale%5D=0&locale_download%5Bencoding%5D=UTF-8 "

        self.download_flutter = 'https://app.phrase.com/accounts/starmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0/projects/' \
                                'starmaker_flutter/locales/download?utf8=%E2%9C%93&locale_names%5B%5D=en&locale_names' \
                                '%5B%5D=ar&locale_names%5B%5D=bn-IN&locale_names%5B%5D=cs&locale_names%5B%5D=de' \
                                '&locale_names%5B%5D=es&locale_names%5B%5D=fr&locale_names%5B%5D=in&locale_names%5B%5D' \
                                '=it&locale_names%5B%5D=ja&locale_names%5B%5D=ko&locale_names%5B%5D=ms&locale_names%5B' \
                                '%5D=pt-BR&locale_names%5B%5D=ru-RU&locale_names%5B%5D=sr&locale_names%5B%5D=th' \
                                '&locale_names%5B%5D=tr-TR&locale_names%5B%5D=ur-PK&locale_names%5B%5D=vi&locale_names' \
                                '%5B%5D=zh-CN&locale_names%5B%5D=zh-TW&locale_download%5Bfile_format%5D=xlsx' \
                                '&locale_download%5Bformat_options%5D%5Bdocument_id%5D=&locale_download' \
                                '%5Bformat_options%5D%5Binclude_headers%5D=0&locale_download%5Bformat_options%5D' \
                                '%5Binclude_headers%5D=1&locale_download%5Bformat_options%5D%5Bexport_tags%5D=0' \
                                '&locale_download%5Bformat_options%5D%5Bexport_system_tags%5D=0&locale_download' \
                                '%5Bformat_options%5D%5Bexport_max_characters_allowed%5D=0&locale_download' \
                                '%5Binclude_empty_translations%5D=0&locale_download%5Binclude_translated_keys%5D=0' \
                                '&locale_download%5Bexclude_empty_zero_forms%5D=0&locale_download' \
                                '%5Binclude_unverified_translations%5D=0&locale_download' \
                                '%5Binclude_unverified_translations%5D=1&locale_download%5Btags%5D%5B%5D' \
                                '=&locale_download%5Bkeep_notranslate_tags%5D=0&locale_download' \
                                '%5Brenders_default_locale%5D=0&locale_download%5Bencoding%5D=UTF-8'
