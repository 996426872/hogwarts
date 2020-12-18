import pytest
import yaml
from com.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("calc.yml", 'r'))['add'])
    def test_add(self, a, b, expect, login):
        print("执行加法{}+{}={}".format(a, b, expect))
        # print(login)
        assert self.calc.add(a, b) == expect
