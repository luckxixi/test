import pytest
#作用域：module是在模块之前执行， 最有一条再调用
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield #第一条时 return返回
    print("执行teardown")
    print("最后关闭浏览器")
def test_search1(open):
    print("test_search1")
    raise NameError
    pass
def test_search2(open):
    print("test_search2")
    raise NameError
    pass
def test_search3(open):
    print("test_search3")
    raise NameError
    pass
if __name__=='__main__':
    pytest.main()