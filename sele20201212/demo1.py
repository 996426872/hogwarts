from selenium import webdriver
import time
driver = webdriver.Chrome()
time.sleep(5)
driver.get("http://www.baidu.com")
time.sleep(5)
driver.quit()