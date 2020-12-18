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
    def test_add(self, a, b, expect):
        assert self.calc.add(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("calc.yml", 'r'))['sub'])
    def test_sub(self, a, b, expect):
        assert self.calc.sub(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("calc.yml", 'r'))['mul'])
    def test_mul(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("calc.yml", 'r'))['div'])
    def test_div(self, a, b, expect):
        assert self.calc.div(a, b) == expect
