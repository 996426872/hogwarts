import pytest


@pytest.mark.usefixtures("cal_begin_end")
class TestCalc:
    @pytest.mark.run(order=1)
    @pytest.mark.add
    def test_add(self, get_calculator, get_add_data):
        print("计算器的内存地址是", id(get_calculator))
        assert get_calculator.add(get_add_data[0], get_add_data[1]) == get_add_data[2]

    @pytest.mark.run(order=3)
    @pytest.mark.sub
    def test_sub(self, get_calculator, get_sub_data):
        print("计算器的内存地址是", id(get_calculator))
        assert get_calculator.sub(get_sub_data[0], get_sub_data[1]) == get_sub_data[2]

    @pytest.mark.run(order=2)
    @pytest.mark.mul
    def test_mul(self, get_calculator, get_mul_data):
        print("计算器的内存地址是", id(get_calculator))
        assert get_calculator.mul(get_mul_data[0], get_mul_data[1]) == get_mul_data[2]

    @pytest.mark.run(order=4)
    @pytest.mark.div
    def test_div(self, get_calculator, get_div_data):
        print("计算器的内存地址是", id(get_calculator))
        assert get_calculator.div(get_div_data[0], get_div_data[1]) == get_div_data[2]
