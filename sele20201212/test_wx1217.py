# coding:utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import yaml
import time
from selenium.common.exceptions import TimeoutException


class TestWx:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        # 打开企业微信
        self.driver.get("https://work.weixin.qq.com/")
        # 加载cookies
        with open("cookie.yml", "r") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def teardown_class(self):
        # 关闭进程
        self.driver.quit()

    def test_login_with_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        self.driver.implicitly_wait(5)
        ele = self.driver.find_element_by_link_text("极简")
        print(ele.text)
        assert ele.text == "极简"

    def test_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        locator_add = ("link text", "添加成员")
        time.sleep(5)
        self.find(locator_add).click()
        time.sleep(5)
        # XPATH = "xpath"
        # LINK_TEXT = "link text"
        # PARTIAL_LINK_TEXT = "partial link text"
        # NAME = "name"
        # TAG_NAME = "tag name"
        # CLASS_NAME = "class name"
        # CSS_SELECTOR = "css selector"
        # #username
        # #memberAdd_acctid
        # #memberAdd_phone
        # text 保存 click
        # username = " "
        # memberAdd_acctid = " "
        # memberAdd_phone = " "
        # 待优化：通讯录page和登录page分开
        # 待优化：数据驱动yaml，封装添加成员函数，传入成员信息参数
        self.driver.find_element("id", "username").send_keys("eee")
        self.driver.find_element("id", "memberAdd_acctid").send_keys("eee")
        self.driver.find_element("id", "memberAdd_phone").send_keys("18300000003")
        self.driver.find_element("link text", "保存").click()
        time.sleep(5)
        # 手机号唯一，可用于定位新的成员
        locator_add_result = ("xpath", "//td[@title='18300000003']")
        tr_element = self.is_element_exist(locator_add_result)
        # 判断新添加的成员手机号
        if tr_element:
            assert tr_element.text == "18300000003"
        else:
            assert tr_element
        time.sleep(5)

    def is_element_exist(self, locator):
        try:
            find_flag = WebDriverWait(self.driver, 20, poll_frequency=0.5, ignored_exceptions=None)\
                .until(lambda x: x.find_element(*locator))
        except TimeoutException:
            # print("{}元素查找失败".format(locator))
            find_flag = False
        # 元素存在则返回元素，否则返回布尔值False
        return find_flag

    def find(self, locator):
        ele = WebDriverWait(self.driver, 20, poll_frequency=0.5, ignored_exceptions=None)\
                .until(lambda x: x.find_element(*locator))
        return ele

    def test_query_member(self):
        pass

    def test_del_member(self):
        pass
