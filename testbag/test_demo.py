import pytest
import yaml
class Testdemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "123" in env:
            print("这是测试环境")
            print(env)
        elif "test" in env:
            print("这是开发环境")
            print("对应的值属性是多少",env["test"])
    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))