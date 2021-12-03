import pytest
def test_a():
    print("执行test——a方法")
class Testdamo():
          def test_one(self):
              print("开始执行test_one方法")
              x='this'
              #assert 'h' in x
              pytest.assume('h' in x)

          def test_two(self):
                print("开始执行test——two 方法")
                x='hello'
                assert 'o' in x
          def test_three(self):
                print("开始执行test——three 方法")
                a='hello'
                b='hellowork'
                assert a  in b
#class Testdamo01():
   #       def test_a(self):
    #            print("开始执行test_a方法")
    #            x='this'
     #           assert 'h' in x
     #     def test_b(self):
        #        print("开始执行test——b 方法")
         #       x='hello'
       #         assert 'o' in x
        #  def test_c(self):
        #        print("开始执行test——c 方法")
         #       a='hello'
          #      b='hellowork'
         #       assert a in b

if __name__=='__main__':
    pytest.main()