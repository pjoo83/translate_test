from selenium import webdriver


class GetDriver:

    def __init__(self):
        self.driver = None

    # 初始化
    def create_driver(self):
        if not self.driver:
            # 无chrome驱动windows系统，使用下列edge()浏览器行代码,苹果电脑使用safari()
            # self.driver = webdriver.Chrome()
            # self.driver = webdriver.Safari()
            self.driver = webdriver.Edge()
            self.driver.maximize_window()
            self.driver.implicitly_wait(15)

            return self.driver

    # 打开页面
    def open_page(self, url):
        base_url = url
        self.driver.get(base_url)

    # 清缓存
    def del_cookie(self):
        cookies = self.driver.get_cookies()
        self.driver.delete_all_cookies()

    #
    # 关闭页面
    def close_page(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    # # 设置文件下载路径
    def set_address(self):
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": 'C://Users//123123//Desktop'}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)
