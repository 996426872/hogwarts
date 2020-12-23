from homework1220.page.index_page import IndexPage


class TestIndex:
    def setup_class(self):
        self.index_page = IndexPage()

    def test_login(self):
        self.index_page.goto_login().login_scanf()

    def test_register(self):
        self.index_page.goto_register().register()
