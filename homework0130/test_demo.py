import requests
import pytest


class TestDemo:
    def test_get_param(self):
        par = {
            "name": "test",
            "password": "1234567890"
        }
        head = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close",
            "User-Agent": "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"
        }
        r = requests.request(method='GET', url='https://httpbin.testing-studio.com/get', params=par, headers=head)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200

    def test_post_form(self):
        par = {
            "name": "test",
            "password": "1234567890"
        }
        head = {
            "Content-Type": "multipart/form-data",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close",
            "User-Agent": "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"
        }
        r = requests.request(method='POST', url='https://httpbin.testing-studio.com/post', data=par, headers=head)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200

    def test_post_xform(self):
        par = {
            "name": "test",
            "password": "1234567890"
        }

        head = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close",
            "User-Agent": "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"
        }
        r = requests.request(method='POST', url='https://httpbin.testing-studio.com/post', data=par, headers=head)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200

    def test_post_json(self):
        par = {
            "name": "test_query",
            "password": "1234567890"
        }
        par_p = {
            "name": "test_post_json",
            "password": "1234567890"
        }
        head = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close",
            "User-Agent": "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"
        }
        r = requests.request(method='POST', url='https://httpbin.testing-studio.com/post', params=par, json=par_p, headers=head)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200