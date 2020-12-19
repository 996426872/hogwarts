import pytest
from homework1209.calculator import Calculator
import yaml

cal = Calculator()
print("计算器的内存地址是", id(cal))
cal_data = yaml.safe_load(open("calc.yml", 'r'))


@pytest.fixture()
def get_calculator():
    return cal


@pytest.fixture(scope="class")
def cal_begin_end():
    print("开始计算")
    yield
    print("结束计算")


@pytest.fixture(params=cal_data['add'])
def get_add_data(request):
    return request.param


@pytest.fixture(params=cal_data['sub'])
def get_sub_data(request):
    return request.param


@pytest.fixture(params=cal_data['mul'])
def get_mul_data(request):
    return request.param


@pytest.fixture(params=cal_data['div'])
def get_div_data(request):
    return request.param




