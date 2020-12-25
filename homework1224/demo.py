from appium import webdriver
import time

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'N8KGY17428000015',
    'platformVersion': '9',
    'appPackage': 'com.taobao.taobao',
    'appActivity': 'com.taobao.tao.welcome.Welcome'
}

desired_caps1 = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'platformVersion': '5.1.1',
    'appPackage': 'com.taobao.taobao',
    'appActivity': 'com.taobao.tao.welcome.Welcome'
}


desired_caps2 = {
    "platformName": "Android",
    "deviceName": "wework",
    "appPackage": "com.tencent.wework",
    "appActivity": ".launch.LaunchSplashActivity",
    "noReset": "true"
}

# “//*[contains(@text,'次外出')]”

driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(10)
