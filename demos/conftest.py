import pytest


@pytest.fixture()
def login():
    print("输入账户密码登录！")


@pytest.fixture()
def logout():
    print("退出登录")
