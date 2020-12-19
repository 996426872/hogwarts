import pytest
import yaml
from homework1209.calculator import Calculator


@pytest.mark.usefixtures("cal_begin_end")
class TestCalc:
    @pytest.mark.run(order=1)
    @pytest.mark.add
    def test_add(self, get_calculator, get_add_data):
        print("计算器的内存地址是", id(get_calculator))
        assert get_calculator.add(get_add_data[0], get_add_data[1]) == get_add_data[2]

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("calc.yml", 'r'))['sub'])
    def test_sub(self, a, b, expect, get_calculator):
        print ("计算器的内存地址是", id(get_calculator))
        assert get_calculator.sub(a, b) == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("calc.yml", 'r'))['mul'])
    def test_mul(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("calc.yml", 'r'))['div'])
    def test_div(self, a, b, expect):
        assert self.calc.div(a, b) == expect
