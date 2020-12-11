import pytest


def add_func(a,b):
    return a+b


@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (1000, -2000, -1000), (1888, 1999, 3887)])
def test_add(a, b, expected):
    assert add_func(a, b) == expected


@pytest.mark.parametrize('a', [1999, 2, 4])
@pytest.mark.parametrize('b', [1999, 8, 1000])
def test_minus(a, b):
    print("测试{}-{}".format(a, b))


class TestMulti:
    # def setup_class(self):
    #     print("类执行一次setup_class")
    #
    # def teardown_class(self):
    #     print("类执行一次teardown_class")

    @classmethod
    def setup_class(cls):
        print("类执行一次setup_class")

    @classmethod
    def teardown_class(cls):
        print("类执行一次teardown_class")

    def test_multi111(self):
        assert 3*4 == 12

    def test_multi222(self):
        assert 3*4 == 12

