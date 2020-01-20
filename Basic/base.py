# coding=utf-8
import random
import allure
import pymysql
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Basic import Log
import os

log = Log.MyLog()


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    # 自定义一个元素查找方法
    def find_element(self, feature, timeout=5, poll=0.5):
        # feature = By.XPATH,"//*[@text='显示']"
        """
        依据用户传入的元素信息特征，然后返回当前用户想要查找元素
        :param feature: 元组类型，包含用户希望的查找方式，及该方式对应的值
        :return: 返回当前用户查找的元素
        """
        by = feature[0]
        value = feature[1]
        wait = WebDriverWait(self.driver, timeout, poll)
        if by == By.XPATH:
            # print( "说明了用户想要使用 xpath 路径的方式来获取元素" )
            value = self.make_xpath(value)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, feature):
        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_elements(feature[0], feature[1]))

    def click_element(self, loc):
        '''
            封装点击操作函数
        '''
        self.find_element(loc).click()

    def input_text(self, loc, text):
        '''
            封装输入操作函数
        '''
        self.fm = self.find_element(loc)
        self.fm.clear()  # 需要先清空输入框，防止有默认内容
        self.fm.send_keys(text)

    # 自定义了一个可以自动帮我们拼接 xpath 路径的工具函数
    def make_xpath(self, feature):
        start_path = "//*["
        end_path = "]"
        res_path = ""

        if isinstance(feature, str):

            # 如果是字符串 我们不能直接上来就拆我们可以判断一下它是否是默认正确的 xpath 写法
            if feature.startswith("//*["):
                return feature

            # 如果用户输入的是字符串，那么我们就拆成列表再次进行判断
            split_list = feature.split(",")
            if len(split_list) == 2:
                # //*[contains(@text,'设')]
                res_path = "%scontains(@%s,'%s')%s" % (start_path, split_list[0], split_list[1], end_path)
            elif len(split_list) == 3:
                # //[@text='设置']
                res_path = "%s@%s='%s'%s" % (start_path, split_list[0], split_list[1], end_path)
            else:
                print("请按规则使用")
        elif isinstance(feature, tuple):
            for item in feature:
                # 默认用户在元组当中定义的数据都是字符串
                split_list2 = item.split(',')
                if len(split_list2) == 2:
                    res_path += "contains(@%s,'%s') and " % (split_list2[0], split_list2[1])
                elif len(split_list2) == 3:
                    res_path += "@%s='%s' and " % (split_list2[0], split_list2[1])
                else:
                    print("请按规则使用")
            andIndex = res_path.rfind(" and")
            res_path = res_path[0:andIndex]
            res_path = start_path + res_path + end_path
        else:
            print("请按规则使用")

        return res_path

    def assert_ele_in(self, text, element):
        '''
            封装断言操作函数
        '''
        try:
            assert text in self.find_element(element).text
            assert 0
        except Exception:
            assert 1

    def get_assert_text(self, element):
        ele = self.find_element(element, timeout=5, poll=0.1)
        return ele.text

    # 自定义一个获取 toast内容的方法
    def get_toast_content(self, message):
        tmp_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        ele = self.find_element(tmp_feature)
        return ele.text

    # 自定义一个工具函数，可以接收用户传递的部分 toast 信息，然后返回一个布尔值，来告诉
    # 用户，目标 toast 到底是否存在
    def is_toast_exist(self, mes):
        # 拿着用户传过来的 message 去判断一下包含该内容的 toast 到底是否存在。
        try:
            # self.get_toast_content(mes)
            data = self.get_toast_content(mes)
            if mes in data:
                return True
        except Exception:
            # 如果目标 toast 不存在那么就说明我们的实际结果和预期结果不一样
            # 因此我们想要的是断言失败
            return False

    def get_toast(self, toast_message):
        message = '//*[@text=\'{}\']'.format(toast_message)
        # 获取toast提示框内容
        toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))

        return toast_element.text

    def is_toast(self, mes):
        try:
            self.get_toast(mes)
            return True
        except Exception as e:
            print(e)
            return False

    def get_xpath(self, value):
        '''封装获取xpath方法'''
        text = By.XPATH, '//*[@text="%s"]' % value
        return text

    # 自定义一个获取当前设备尺寸的功能
    def get_device_size(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return x, y

    # 自定义一个功能，可以实现向左滑屏操作。
    def swipe_left(self):
        start_x = self.get_device_size()[0] * 0.9
        start_y = self.get_device_size()[1] * 0.5
        end_x = self.get_device_size()[0] * 0.4
        end_y = self.get_device_size()[1] * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y, 200)

    # 自定义一个功能，可以实现向上滑屏操作。
    def swipe_up(self):
        start_x = self.get_device_size()[0] * 1/2
        start_y = self.get_device_size()[1] * 1/2
        end_x = self.get_device_size()[0] * 1/2
        end_y = self.get_device_size()[1] * 1/7
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)

    # 切换到微信
    def switch_weixxin(self):
        self.driver.start_activity("com.tencent.mm", ".ui.LauncherUI")

    def switch_webview(self):
        # 切换到webview
        self.driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
        print("切换成功")

    # 自定义根据坐标定位
    def taptest(self, a, b):
        # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
        # 获取当前手机屏幕大小X,Y
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        self.driver.tap([(a * X, b * Y)])

    # 自定义截图函数
    def take_screenShot(self):
        '''
        测试失败截图，并把截图展示到allure报告中
        '''
        tm = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        self.driver.get_screenshot_as_file(
            os.getcwd() + os.sep + "image/%s.png" % tm)
        allure.attach.file(os.getcwd() + os.sep + "image/%s.png" %
                           tm, attachment_type=allure.attachment_type.PNG)

    # 自定义随机生成11位手机号
    def create_phone(self):
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)


