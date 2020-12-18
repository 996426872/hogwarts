import pytest


@pytest.fixture(params=['第一个参数', '第二个参数', '第三个参数'])
def login(request):
    print(request.param)
    yield
    print("退出登录")



@pytest.fixture()
def logout():
    print("退出登录")
