from homework1220.page.add_member_page import AddMember
from homework1220.page.contact_page import ContactPage
from selenium import webdriver


class MainPage:
    def __init__(self, driver):
        self.driver = driver.

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        add_member_loc = ("css selector", ".ww_indexImg_AddMember")
        return AddMember()

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        return ContactPage()
