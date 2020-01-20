from time import sleep
from Basic.base import Base
from selenium.webdriver.common.by import By
from Basic.config import myconfig


class Login_Page(Base):
    """登录"""
    # 手机号
    user_feature = By.XPATH, '//*[@text="手机号码"]'
    # 密码
    pwd_feature = By.XPATH, "//*[@text='密码']"
    # 登陆
    click_login_feature = By.XPATH, '//*[@content-desc="login"]'
    # 保存账号
    save_user_feature = By.XPATH, '//*[@text="保存"]'
    # 手机号快速注册
    sign_in_feature = By.XPATH, '//*[@text="手机号快速注册"]'
    # 验证码
    auth_code_feature = By.XPATH, '//*[@text="验证码"]'
    # 下一步
    next_step_feature = By.XPATH, '//*[@text="下一步"]'
    # 输入密码
    enter_password_feature = By.XPATH, '//*[@text="输入密码"]'
    # 确认密码
    confirm_password_feature = By.XPATH, '//*[@text="确认密码"]'
    # 用户协议
    user_agreement_feature = By.XPATH, '//*[@text="我已同意柔济健康用户协议"]'
    # 同意用户协议
    read_agreed_feature = By.XPATH, '//*[@text="我已阅读并同意柔济健康用户协议"]'
    # 完成注册
    complete_registration_feature = By.XPATH, '//*[@content-desc="regok"]'
    # 获取验证码
    get_code_feature = By.XPATH, '//*[@text="获取验证码"]'
    # 忘记密码
    forget_the_password_feature = By.XPATH, '//*[@text="忘记密码"]'
    # 完成
    accomplish_feature = By.XPATH, '//*[@text="完成"]'
    # 注册的手机号
    register_user_feature = By.XPATH, '//*[@content-desc="number"]'

    def input_user(self, value):
        # 输入用户名
        self.input_text(self.user_feature, value)

    def error_register(self, value):
        self.input_text(self.register_user_feature, value)

    def create_user(self):
        users = self.create_phone()
        user = str(users)
        self.input_text(self.register_user_feature, user)

    def input_pwd(self, value):
        # 输入密码
        self.input_text(self.pwd_feature, value)

    def click_login(self):
        # 点击登录
        self.click_element(self.click_login_feature)

    def click_save_user(self):
        # 点击保存账号
        self.click_element(self.save_user_feature)

    def login(self):
        '''登陆函数'''
        self.input_user(myconfig.username)
        self.input_pwd(myconfig.password)
        self.click_login()
        sleep(1)
        self.click_save_user()

    # 点击手机号快速注册
    def sign_in(self):
        self.click_element(self.sign_in_feature)

    # 点击输入验证码
    def input_auth_code(self, value):
        self.input_text(self.auth_code_feature, value)

    # 点击下一步
    def click_next_step(self):
        self.click_element(self.next_step_feature)

    # 点击输入密码
    def input_enter_password(self, value):
        self.input_text(self.enter_password_feature, value)

    # 点击输入确认密码
    def input_confirm_password(self, vaule):
        self.input_text(self.confirm_password_feature, vaule)

    # 点击用户协议
    def click_user_agreement(self):
        self.click_element(self.user_agreement_feature)

    # 点击阅读同意用户协议
    def click_read_agreed(self):
        self.click_element(self.read_agreed_feature)

    # 点击完成注册
    def click_complete_registration(self):
        self.click_element(self.complete_registration_feature)

    # 点击获取验证码
    def click_get_code(self):
        self.click_element(self.get_code_feature)

    # 点击忘记密码
    def forget_the_password(self):
        self.click_element(self.forget_the_password_feature)

    # 点击完成
    def click_accomplish(self):
        self.click_element(self.accomplish_feature)
