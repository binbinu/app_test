# coding=utf-8
import allure
from Basic.config import myconfig
from Basic.deiver import init_driver
from Basic.get_data import getData
from Page.page import Page
import pytest


@allure.severity(allure.severity_level.BLOCKER)
class Test_login:
    '''登陆注册找回密码'''

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.users = self.page.initloginpage.create_phone()
        self.user = str(self.users)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        '''正确登陆'''
        self.page.initloginpage.input_user(myconfig.username)
        self.page.initloginpage.input_pwd(myconfig.password)
        self.page.initloginpage.click_login()
        self.page.initloginpage.click_save_user()
        data = self.page.inithomepage.home_page()
        assert data == "首页"

    @pytest.mark.parametrize(
        "args", getData("test_login_error", 'data_error_login'))
    def test_error_login(self, args):
        """错误登陆"""
        self.page.initloginpage.input_user(args[0])
        self.page.initloginpage.input_pwd(args[1])
        self.page.initloginpage.click_login()
        toast_status = self.page.initloginpage.is_toast_exist(args[2])
        assert toast_status

