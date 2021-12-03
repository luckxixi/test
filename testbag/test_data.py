import  pytest
import yaml
class Testdata():
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def testdata(self,a,b):
        print(a+b)
