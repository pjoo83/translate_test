from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 获取当前页面地址
    def page_url(self):
        return self.driver.current_url

    # 查找定位
    def base_find(self, loc, timeout=60, poll=0.5):
        if len(loc) > 2:
            try:
                return WebDriverWait(self.driver, timeout=timeout,
                                     poll_frequency=poll).until(
                    lambda x: self.driver.find_elements(loc[0], loc[1])[loc[2]])
            except IndexError:
                print("定位元素未找到" + str(loc))
        else:
            return WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll).until(ec.presence_of_element_located(loc),
                                                            message="定位元素未找到" + str(loc))

    # 点击方法
    def base_click(self, loc):
        el = self.base_find(loc)
        el.click()

    # 输入
    def base_input(self, loc, value):
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 显示等待
    def wait_time(self, loc):
        WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located(loc))
