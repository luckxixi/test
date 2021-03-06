import pytest
import allure
from selenium import webdriver
import time
@allure.testcase("http://www.github.com",name='测试用例管理地址')
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',['allure','pytest','unitest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):#步骤说明
         driver=webdriver.Chrome()
         driver.get("http://www.baidu.com")
         driver.maximize_window()
    with allure.step(f"请输入搜索词：{test_data1}"):
         driver.find_element_by_id("kw").send_keys(test_data1)
         time.sleep(2)
         driver.find_element_by_id("su").click()
         time.sleep(2)

    with allure.step("保存图片"):
         driver.save_screenshot("./result/b.png")
         allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
         #allure.attach("<head></head><body>首页</body>",'attach with HTML type',attachment_type=allure.attachment_type.HTML)
    with allure.step("关闭浏览器"):
         driver.quit()
