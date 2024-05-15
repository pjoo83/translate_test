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
        self.download_android = "https://app.phrase.com/accounts/starmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0" \
                                "/projects/starmaker-android/locales/download?locale_names%5B%5D=en&locale_names%5B" \
                                "%5D=ar&locale_names%5B%5D=bn&locale_names%5B%5D=cs&locale_names%5B%5D=de" \
                                "&locale_names%5B%5D=es&locale_names%5B%5D=fr&locale_names%5B%5D=in&locale_names%5B" \
                                "%5D=it&locale_names%5B%5D=ja&locale_names%5B%5D=ko&locale_names%5B%5D=ms" \
                                "&locale_names%5B%5D=pt-rBR&locale_names%5B%5D=ru&locale_names%5B%5D=ru-rRU" \
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
                                "&locale_download%5Bencoding%5D=UTF-8"
        # 请求IOS多语言文件
        self.download_ios = "https://app.phrase.com/accounts/starmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0/projects" \
                            "/starmaker-ios/locales/download?locale_names%5B%5D=en&locale_names%5B%5D=ar&locale_names" \
                            "%5B%5D=bn&locale_names%5B%5D=bn-IN&locale_names%5B%5D=de&locale_names%5B%5D=es" \
                            "&locale_names%5B%5D=fr&locale_names%5B%5D=id&locale_names%5B%5D=it&locale_names%5B%5D=ja" \
                            "&locale_names%5B%5D=ko&locale_names%5B%5D=ms&locale_names%5B%5D=pt-BR&locale_names%5B%5D" \
                            "=ru-RU&locale_names%5B%5D=th&locale_names%5B%5D=tr-TR&locale_names%5B%5D=ur-PK" \
                            "&locale_names%5B%5D=vi&locale_names%5B%5D=zh-CN&locale_names%5B%5D=zh-Hant&locale_names" \
                            "%5B%5D=zh-TW&locale_download%5Bfile_format%5D=xlsx&locale_download%5Bformat_options%5D" \
                            "%5Bdocument_id%5D=&locale_download%5Bformat_options%5D%5Binclude_headers%5D=0" \
                            "&locale_download%5Bformat_options%5D%5Binclude_headers%5D=1&locale_download" \
                            "%5Bformat_options%5D%5Bexport_tags%5D=0&locale_download%5Bformat_options%5D" \
                            "%5Bexport_system_tags%5D=0&locale_download%5Bformat_options%5D" \
                            "%5Bexport_max_characters_allowed%5D=0&locale_download%5Binclude_empty_translations%5D=0" \
                            "&locale_download%5Binclude_translated_keys%5D=0&locale_download" \
                            "%5Bexclude_empty_zero_forms%5D=0&locale_download%5Binclude_unverified_translations%5D=0" \
                            "&locale_download%5Binclude_unverified_translations%5D=1&locale_download" \
                            "%5Buse_last_reviewed_version%5D=0&locale_download%5Btags%5D%5B%5D=&locale_download" \
                            "%5Bkeep_notranslate_tags%5D=0&locale_download%5Brenders_default_locale%5D=0" \
                            "&locale_download%5Bencoding%5D=UTF-8"

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

        self.download_common_cookie ='_zitok=21a3db1bd27f06fe666f1688783650; OptanonAlertBoxClosed=2023-07-08T03:15:23.870Z; _pa_vid=1iahl6c-cv18-fhtjpd; uid=0945ddc4ee284f9401e5d94f866bf26e; _hjSessionUser_3270412=eyJpZCI6IjUzN2E1NDgyLTY4N2MtNTg5My1iYmY4LWRiNDE1N2IxNDIxZiIsImNyZWF0ZWQiOjE2ODg3ODYxMjQ2MzYsImV4aXN0aW5nIjp0cnVlfQ==; language=en; hubspotutk=567cf3f4d9a2b2275d482417a49fe121; intercom-id-qnzpmkdl=b8323223-293d-4c32-b7cf-5dfa46637777; intercom-device-id-qnzpmkdl=2be27183-ad2b-488a-9690-ab401bbfee8e; _pa_iid=ldm9min0; _fbp=fb.1.1709190673381.1977561661; _ga_KGJ9S35JX0=GS1.2.1709633514.5.1.1709633616.49.0.0; _gcl_au=1.1.158325581.1713953564; _ga=GA1.1.1186896170.1688786138; __hssrc=1; current_identity=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltWTNaRGsyTUdSbE5UVmpNVGszTjJFMk16UmxORGt5TXpkaE56UmpORFl6SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfaWRlbnRpdHkifX0%3D--a6efcbdbc5e6d1940ffd090f81fad56039b45000; current_account=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltTTVPRFF4TkRCallUQTBPVFl3TkRJek1tVXlZMlU1TTJJd01HUTJaV0U1SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfYWNjb3VudCJ9fQ%3D%3D--96da6ef4d0f1ca867607cf80c6be83b7c3081ee1; __hstc=24829477.567cf3f4d9a2b2275d482417a49fe121.1688786223073.1715661141537.1715667388156.14; _uetsid=7411953011a411efa65be7e1546d61de; _uetvid=b8a88450d6d111eeb9bfd53d6be3dd73; _ga_J2EQJSNGG3=GS1.1.1715666949.11.1.1715671380.0.0.0; mp_7ee5623b0363d19908a81c8e4e3a62a7_mixpanel=%7B%22distinct_id%22%3A%20%220945ddc4ee284f9401e5d94f866bf26e%22%2C%22%24device_id%22%3A%20%2218e0cb97295507-0054098581536e-1e525637-201b88-18e0cb97295507%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.phrase.com%2Faccounts%2Fstarmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0%2Fprojects%2Fstarmaker-server%2Flocales%22%2C%22%24initial_referring_domain%22%3A%20%22app.phrase.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%220945ddc4ee284f9401e5d94f866bf26e%22%2C%22Trial%22%3A%20false%2C%22Account%20Code%22%3A%20%22c984140ca049604232e2ce93b00d6ea9%22%2C%22Account%20Status%22%3A%20%22paying%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Wed+May+15+2024+10%3A40%3A13+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202209.2.0&isIABGlobal=false&hosts=&consentId=4cb168b0-ec77-4209-943b-c9f3174539da&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CN%3BBJ&AwaitingReconsent=false; _phrase_session_sec=AKafFEUcLTM6bHqcunuaNEEATqu78ZgoknDQVKO4VrdXG769txWxomutBjXDyLBT7welnPXyEjbaJIatqF6Hnd9CsxGNfqR4%2F%2FU%2BdPwcOndAU%2BaZCLiqeOMMWTjPC71kjTJeEp6ZKg2cFEZhfFwL0XbEEb12RPs5a5MxGqVqo50S72lE84Ls%2B49UvsxF5q7sSyNz3VqIMshTLzQ8geaTfDEKivwAQQAOkr1EIMI9vOfp01kB4cbCtyu5Vhlz1Y0OBmZ4KMlB4lwAfMuwWyOlCVgkh6YJ8VE8o0h9ZvImEMlkXGh0bpclnTlUkxDYicybi7WGSDn9Uubavk0RMPcyPfD%2FJbn54SBgHlV1CUiOWcCSVpvdYEGA3Jq7KLISbrdeQd%2Bwj7XsUMN%2FZtYrUmK%2BEGdB2c%2Fruzd1ojyF9ZzdXaSgo%2FMkesPBLgIC25sNAagU%2B3wul2Th4rQsVvB%2Fl4Tt9gt4zPFqRmBJbkC1LofTT2W%2FFKo17UgAFPfWZYCBt5plZqcmx%2BMpeP4z%2FsvgPv3ox8jaJedg8EYoMbq9SU4AubThj4Imdqcmvhx4UlDALWf%2BZLP3T5GAPU7Gj67vK%2BqjoIOMe7v7aX5Rg0613DeY0P%2Fyu9jbMco45Yeg%2BY76%2BjmdnE1Xf0bHasBruM%2F9YZPJ3pXunPJzIzp6kYQGC2BMNRuhfLnvFDLOGkN2Jr6pjyuYXuwLMtD3C%2F35r7VV6bAfUZ7Bj%2FlBLrYHd2qZs5nxKlMsreGDmlAASu4xpISurxvstUEZclDpD%2BlVYwLK%2F5YsRoSl7ebOVmRUm%2B%2Bd%2BwnVyujSG5Y%2BZtmV8aIWC6NWGZFW3MA7K2gjhotsQ0X3hhSfh%2FQIlEkt508bvK0cpzvtCVWPE%2BWkikopo4My7nGg05Kt%2BtB4a3j0tnBUo6dRUxIEZ7MiCasisxzddDupv%2BlukpS8sRDzKBSqPDEhyX9s--DT5hHNn9uthymvEg--X5jFID2L1HM6QJERYTDB4Q%3D%3D'
        self.download_android_cookie = '_zitok=21a3db1bd27f06fe666f1688783650; OptanonAlertBoxClosed=2023-07-08T03:15:23.870Z; _pa_vid=1iahl6c-cv18-fhtjpd; uid=0945ddc4ee284f9401e5d94f866bf26e; _hjSessionUser_3270412=eyJpZCI6IjUzN2E1NDgyLTY4N2MtNTg5My1iYmY4LWRiNDE1N2IxNDIxZiIsImNyZWF0ZWQiOjE2ODg3ODYxMjQ2MzYsImV4aXN0aW5nIjp0cnVlfQ==; language=en; hubspotutk=567cf3f4d9a2b2275d482417a49fe121; intercom-id-qnzpmkdl=b8323223-293d-4c32-b7cf-5dfa46637777; intercom-device-id-qnzpmkdl=2be27183-ad2b-488a-9690-ab401bbfee8e; _pa_iid=ldm9min0; _fbp=fb.1.1709190673381.1977561661; _ga_KGJ9S35JX0=GS1.2.1709633514.5.1.1709633616.49.0.0; _gcl_au=1.1.158325581.1713953564; _ga=GA1.1.1186896170.1688786138; __hssrc=1; current_identity=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltWTNaRGsyTUdSbE5UVmpNVGszTjJFMk16UmxORGt5TXpkaE56UmpORFl6SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfaWRlbnRpdHkifX0%3D--a6efcbdbc5e6d1940ffd090f81fad56039b45000; current_account=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltTTVPRFF4TkRCallUQTBPVFl3TkRJek1tVXlZMlU1TTJJd01HUTJaV0U1SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfYWNjb3VudCJ9fQ%3D%3D--96da6ef4d0f1ca867607cf80c6be83b7c3081ee1; __hstc=24829477.567cf3f4d9a2b2275d482417a49fe121.1688786223073.1715661141537.1715667388156.14; _uetsid=7411953011a411efa65be7e1546d61de; _uetvid=b8a88450d6d111eeb9bfd53d6be3dd73; _ga_J2EQJSNGG3=GS1.1.1715666949.11.1.1715671380.0.0.0; mp_7ee5623b0363d19908a81c8e4e3a62a7_mixpanel=%7B%22distinct_id%22%3A%20%220945ddc4ee284f9401e5d94f866bf26e%22%2C%22%24device_id%22%3A%20%2218e0cb97295507-0054098581536e-1e525637-201b88-18e0cb97295507%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.phrase.com%2Faccounts%2Fstarmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0%2Fprojects%2Fstarmaker-server%2Flocales%22%2C%22%24initial_referring_domain%22%3A%20%22app.phrase.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%220945ddc4ee284f9401e5d94f866bf26e%22%2C%22Trial%22%3A%20false%2C%22Account%20Code%22%3A%20%22c984140ca049604232e2ce93b00d6ea9%22%2C%22Account%20Status%22%3A%20%22paying%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Wed+May+15+2024+10%3A43%3A12+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202209.2.0&isIABGlobal=false&hosts=&consentId=4cb168b0-ec77-4209-943b-c9f3174539da&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CN%3BBJ&AwaitingReconsent=false; _phrase_session_sec=mL%2F4DdTrQAnPtq6sGeArwXc6dSa7Osylmm4lh%2B3URkh8z5IykYBPr49neke07CBLbVUb34jlVLTKOjpP%2BVP3wStRe1ZDXnWSYuc9%2BRJzEz1HOkGeFYXS3G6V9LpN56lJK8mlVrctqoQKFxS9eVe9F5XnAfEw8AovKOP%2F8XIN3mcBXoNoScyo3pYGrEs%2Bq5qkW7I0t8%2FClHtSxZHsrbbIqGU37%2F7G80yIILoSn5jmBrcjs0DjKqkWd4M4Cw64jYg8ZxUrUpFWM5paH1FbiVeJndzvhE5V3VU4U4Ql6WF4Pp4XjiAaRdFi3oNB%2B1LPFTmJA7GpCskvZnJvuJFTsGaHaiwBrj39BI0G8yqiQKUcM2DRR46lfBSAvy0wdWOXGkUtjSBK11NFMQf8vLKGCCi2jKbAu0ctYTrx0lhw0Jz59X9yzWWF2GAGcdps0ZYDLKaPFkwsWr143NyXi2PzJu1n6r0iwnNGNXI%2BonS3x1e%2F7g4lTZZUs04qfCNG0YxGKRHAeRABAtO%2BKaSO1vpFa8IvKqbl5eNCeDZ4SuJFZskZxyTQzsCRf5lX%2FWHFN3oH6u8c3WduNt%2BimoAfaTvPX5gAJOFRSGr9yTFNLtk%2FKsX9IlA2wj%2FJXR9nWyNcDfzq2UNDEeoL%2FSbgfAWlAmTTqmo8GkfJW1NJN1RzLPaCEO06YbCESQ2v%2FHF%2BJ7r42pzU%2BHrnSxFBNetLe%2Fi8dCZIRZ5J8YmhnljN%2F4xVRzkIEg33hquiCw9tkPCn%2FqBH0IstQEVFJLllEEomLMOoxnms%2FD%2B5U4AfDu7m7kf0RZu3DhbbfUMm9dpqQjaykrLC7cn56Iuxp2N5emWLM9Z9Gqlz%2FS9Can%2FYyPEIw%2Fpmx4C7tsbpOdJwKyEXG8cR%2FXb2PuV%2BhpiySee1D6lLSizaiM1DEHV7oN%2FrlsZNyZXSQ9IIQ21cK8K3b7Qh4Uiewpi8CLy9--xshkJ3BIaSS1am3K--bn3mrVxCFBPjjPTWlMTuNA%3D%3D'
        self.download_ios_cookie = '_zitok=21a3db1bd27f06fe666f1688783650; OptanonAlertBoxClosed=2023-07-08T03:15:23.870Z; _pa_vid=1iahl6c-cv18-fhtjpd; uid=0945ddc4ee284f9401e5d94f866bf26e; _hjSessionUser_3270412=eyJpZCI6IjUzN2E1NDgyLTY4N2MtNTg5My1iYmY4LWRiNDE1N2IxNDIxZiIsImNyZWF0ZWQiOjE2ODg3ODYxMjQ2MzYsImV4aXN0aW5nIjp0cnVlfQ==; language=en; hubspotutk=567cf3f4d9a2b2275d482417a49fe121; intercom-id-qnzpmkdl=b8323223-293d-4c32-b7cf-5dfa46637777; intercom-device-id-qnzpmkdl=2be27183-ad2b-488a-9690-ab401bbfee8e; _pa_iid=ldm9min0; _fbp=fb.1.1709190673381.1977561661; _ga_KGJ9S35JX0=GS1.2.1709633514.5.1.1709633616.49.0.0; _gcl_au=1.1.158325581.1713953564; _ga=GA1.1.1186896170.1688786138; __hssrc=1; current_identity=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltWTNaRGsyTUdSbE5UVmpNVGszTjJFMk16UmxORGt5TXpkaE56UmpORFl6SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfaWRlbnRpdHkifX0%3D--a6efcbdbc5e6d1940ffd090f81fad56039b45000; current_account=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltTTVPRFF4TkRCallUQTBPVFl3TkRJek1tVXlZMlU1TTJJd01HUTJaV0U1SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfYWNjb3VudCJ9fQ%3D%3D--96da6ef4d0f1ca867607cf80c6be83b7c3081ee1; __hstc=24829477.567cf3f4d9a2b2275d482417a49fe121.1688786223073.1715661141537.1715667388156.14; _uetsid=7411953011a411efa65be7e1546d61de; _uetvid=b8a88450d6d111eeb9bfd53d6be3dd73; _ga_J2EQJSNGG3=GS1.1.1715666949.11.1.1715671380.0.0.0; mp_7ee5623b0363d19908a81c8e4e3a62a7_mixpanel=%7B%22distinct_id%22%3A%20%220945ddc4ee284f9401e5d94f866bf26e%22%2C%22%24device_id%22%3A%20%2218e0cb97295507-0054098581536e-1e525637-201b88-18e0cb97295507%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.phrase.com%2Faccounts%2Fstarmaker-319c9ca6-0e8d-4fa3-8fa2-1ca0ea7692f0%2Fprojects%2Fstarmaker-server%2Flocales%22%2C%22%24initial_referring_domain%22%3A%20%22app.phrase.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%220945ddc4ee284f9401e5d94f866bf26e%22%2C%22Trial%22%3A%20false%2C%22Account%20Code%22%3A%20%22c984140ca049604232e2ce93b00d6ea9%22%2C%22Account%20Status%22%3A%20%22paying%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Wed+May+15+2024+10%3A44%3A54+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202209.2.0&isIABGlobal=false&hosts=&consentId=4cb168b0-ec77-4209-943b-c9f3174539da&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=CN%3BBJ&AwaitingReconsent=false; _phrase_session_sec=rad0cGOW7vcUMDrUDXo6rUFi5aw2rvDP30UHc%2Bf55HoByWfnsy1bZm5u0NwECbNKJT21ai7Zyp3fLM134YSlCenHYz%2BY2fZcTIOtwqNazNRIcEyHUq89rUguqvRCsrAoHIHVLs2ylOkiiBS1pxT%2B48NgWjsXSEu%2BEvt0XTbJYCewyTAW%2FOH7RM0VyV43FD6kB8vzbCSAdqQ3Es4QQnGugg3q8tOHiuBhbTiTNmXQd9X0bM%2BTqdHTX%2B%2Bql6%2FsUAPfEQo%2FeAmQ77wSe8l5lliBCHB5q3MvQ5L8Ur4SCl3%2B0a2VFDjQQTmV%2BlomPaKklHuy1lS4G%2BpzrHik5ktm9hhjzNmS2TpMmSWnEPQ69AFzdu%2FyXzF8I0AJ1aUEKIUGkk%2Fqp0Wlo6eEBbAvZ4zkXXWEjScC8ZJxAC7JjyhMiy5LJppBsLz%2BsAjYhI2ZC6vDGf3c%2FWlHXrHTVZ0ThpPSk4ED9P%2BaqSFpt0D9xQGRqdyJnNuL4uIomC3hUrxblyrwmDUHcSZc%2BUPBlNXVwxnZhv%2BSTcaytLTAB13Chfwo4NDj9CsdoFCKgErR5D%2FFAcBOkTfoRcmmKoeN%2F9VpR7uKhkIrmiClREhDmyrMfS80ai%2FUVtcMFjP1aEp%2Fxh6RNAnMaBpbPjM6kEnv8REMUt8AOTxyjFN2ZdPINJY%2BEhhSHiefwTvcJLF6UH1QzQt2P1qxYBZJVlJPrQ61NgsZaDIvd2BxfVSvmfPjKHOCbAI0Nnx4tEFbua%2FtlBsuDx6s%2BesY07zlY3%2FsNBvpbJ16nkVKCv%2BM95fiXph3j5xBtLZq9Id1cv578ejLiAA5%2F4Qh8Lz7YYvvDcvA7M0iZG39ei5vwcMf3fb0ESadnmJvKWrfydo%2BMn7BLjN7aC4KuMW3TGHIrChswFiMI%2FdjmpK2m9REOmKP3GmgxVqXR1Bhge%2F%2Bez%2F1MWnbEBJKXVV4atsudSAL--HN%2FHqtKZqOXGVxVf--bdH4EIdw3FnPl%2BMPwFNDDQ%3D%3D'
