from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChormeService
from webdriver_manager.chrome import ChromeDriverManager


"""
接口测试计划
    华测商城接口
        用户  注册，登录
        商品  添加购物车，立即购买
        订单  取消，支付
"""

class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome(ChormeService(ChromeDriverManager().install()))

    # 打开地址
    def get_url(self, url):
        self.driver.get(url)

    # 输入内容
    def sends(self, selector, value):
        return self.driver.find_element(*selector).send_keys(value)

    # 点击
    def click(self, selecto):
        self.driver.find_element(*selecto).click()

    # 退出
    def quit(self):
        self.driver.quit()
