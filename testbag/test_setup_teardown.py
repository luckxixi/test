import pytest

def setup_moudle():
    print("这是个 SETUP_MODULE方法")
def teardown_moudle():
    print("这是一个teardown_module方法")
def setup_function():
    print("这是一个 setup_function 方法")
def teardown_function():
    print("这是一个 teardown_function 方法")
def test_login():
    print("这是一个外部的方法")
class Testdemo():
    def setup_class(self):
        print("setup_class")
    def setup_method(self):
        print("setup_method")
    def setup(self):
        print("setup")
    def teardown_class(self):
        print("teardown_class")
    def teardown_method(self):
        print("teardown_method")
    def teardown(self):
        print("teardown")
    def test_one(self):
        print("开始执行test_one方法")
        x = 'this'
        # assert 'h' in x
        pytest.assume('h' in x)
    def test_two(self):
        print("开始执行test——two 方法")
        x = 'hello'
        assert 'o' in x
    def test_three(self):
        print("开始执行test——three 方法")
        a = 'hello'
        b = 'hellowork'
        assert a in b
if __name__=='__main__':
     pytest.main()