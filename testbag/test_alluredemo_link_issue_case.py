import allure

@allure.link("http://www.baidu.com",name="链接")
def test_with_link():
    print("这是一条加链接的测试")
    pass