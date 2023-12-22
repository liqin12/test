from time import sleep

from base.BasePage import BasePage

from selenium.webdriver.common.by import By


class Train_official(BasePage):
    login_but = (By.ID, 'J-btn-login')  # 点击登录页面
    username = (By.ID, 'J-userName')
    password = (By.ID, 'J-password')
    but_login = (By.ID, 'J-login')  # 登录按钮

    def login(self, username, password):
        self.click(self.login_but)
        sleep(3)
        self.sends(self.username, username)
        self.sends(self.password, password)
        sleep(5)
        self.click(self.but_login)


if __name__ == '__main__':
    tlg = Train_official()
    tlg.get_url('https://www.12306.cn/index/')
    tlg.login('13628097436', 'liqin_199512')
