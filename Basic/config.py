# coding=utf-8
"""
读取全局变量配置
"""

import os
from configparser import ConfigParser

PATH = os.getcwd()
CONFIG_FILE_PATH = os.path.join(PATH, "config.ini")  # 配置文件名称


class MyConfig:
    def __init__(self):

        config = ConfigParser()
        config.read(CONFIG_FILE_PATH, 'utf-8')

        # 配置环境，SCE是生成环境, PE是测试环境
        self.environment = config.get("config", "environment")
        # 用户名手机号
        self.username = config.get("data", "username")
        # 密码
        self.password = config.get("data", "password")
        # 验证码
        self.auth_code = config.get("data", "auth_code")
        # 错误密码
        self.error_pwd = config.get("data", "error_pwd")
        # 错误五位数密码
        self.five_pwd = config.get("data", "five_pwd")


myconfig = MyConfig()

