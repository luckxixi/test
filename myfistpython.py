from selenium import webdriver
from time import sleep
import unittest
class TestHogwards(unittest.TestCase):
    def setup(self):
       self.driver = webdriver.Chrome()
       self.driver.maximize.window()
    def teardown(self):
       self.driver.quit()
    def test_hogwards(self):
       self.driver.get("http://www.testerhome.com")
       sleep(1)
       self.driver.find_element_by_link_text("社团").click()
       sleep(1)
       self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
       sleep(1)
       self.driver.find_element_by_css_selector(".topic-22621 .title > a").click()
       sleep(1)