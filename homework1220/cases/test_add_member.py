from selenium import webdriver
from homework1220.page.contact_page import ContactPage
from homework1220.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        driver = webdriver.Chrome()
        self.main_page = MainPage(driver)

    def test_add_member_from_main_page(self):
        self.main_page.goto_add_member().add_member().get_members()

    def test_add_member_from_contact_page(self):
        self.main_page.goto_contact().add_member()
