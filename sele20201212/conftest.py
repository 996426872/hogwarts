import pytest
import yaml
from selenium import webdriver


@pytest.fixture(scope="class",autouse="True")
def get_cookies():
    option = webdriver.ChromeOptions()
    option.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/")
    driver.implicitly_wait(5)
    cookies = driver.get_cookies()
    print(cookies)
    with open("cookie.yml", "w") as f:
        yaml.dump(cookies, f)
    driver.quit()


