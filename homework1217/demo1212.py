# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCeshiren:
    def setup_method(self, method):
       self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_category(self):
        self.driver.get("https://ceshiren.com")
        sleep(5)
        # 注意当前为未登录状态下的菜单
        # self.driver.get_screenshot_as_file(r"C:\hogwarts\homework1217\screen.jpg")
        # action = ActionChains(self.driver)
        # xpath 标签名字 属性 定位
        self.driver.find_element_by_xpath("//div[@title='所有分类']").click()
        sleep(5)

        # # 这段定位元素代码通过测试
        # category_list = self.driver.find_elements_by_css_selector(".category-name")
        # find_category = None
        # for category in category_list:
        #     if category.text == '霍格沃兹公开课':
        #         print(category.text)
        #         find_category = category
        #         break
        # find_category.click()

        # print(self.driver.find_element_by_xpath("//span[@class='category-name' and contains(text(),'霍格沃兹公开课')]").text)

        # 模糊匹配contains text()，测试通过
        category = self.driver.find_element_by_xpath("//span[contains(text(),'霍格沃兹公开课')]")


        # 获取元素属性，测试通过
        print("attribute:", category.get_attribute('class'))
        print("location:", category.location)
        print("size:", category.size)

        category.click()

        # # 通过链接的文本匹配，未通过测试，看看哪里有问题
        # self.driver.find_element_by_partial_link_text('霍格沃兹公开课').click()

        sleep(5)
        self.driver.refresh()
        sleep(5)
        print(self.driver.page_source)
        sleep(5)
        self.driver.minimize_window()
        sleep(5)
        self.driver.maximize_window()
        sleep(5)
        self.driver.set_window_size(1000, 1000)
        sleep(5)

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('上海悠悠')
        sleep(5)

        # submit一般都是模拟输入enter键，测试通过
        # self.driver.find_element_by_id ('kw').submit()

        # 输入enter键，测试通过
        # self.driver.find_element_by_id('kw').send_keys(Keys.ENTER)

        # 点击第一条，测试通过
        # self.driver.find_element_by_id('su').click()
        # sleep(5)
        # a = self.driver.find_element_by_xpath('//div[@id="content_left"]/div[1]/h3/a')
        # print(a.text)
        # a.click()

        sleep(5)

    def test_handle(self):
        self.driver.get("https://wwww.baidu.com")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('上海悠悠')
        sleep(3)
        # 点击第一条，测试通过
        self.driver.find_element_by_id('su').click()
        sleep(3)
        a = self.driver.find_element_by_xpath('//div[@id="content_left"]/div[1]/h3/a')
        print(a.text)
        a.click()
        sleep(3)
        print(self.driver.window_handles)
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(3)
        print(self.driver.title)
        sleep(3)



