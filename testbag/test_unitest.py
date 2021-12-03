import unittest
class demo(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
          print("setup class")
      @classmethod
      def tearDownClass(cls):
          print("teardown class")
      def setUp(self):
          print("setup")
      def tearDown(self):
          print("teardown")
      def test_case01(self):
          print("testcase01")
          self.assertEqual(2,2,"判断相等") #断言2个值相等
          self.assertIn('s','this')
          #assertin   断言

      def test_case02(self):
          print("testcase02")
          self.assertEqual(3, 3, "判断相等")  # 断言2个值相等
         # self.assertIn('h', 'this')

      @unittest.skipIf(1+1==2,"跳过这条测试用例")
      def test_case03(self):
          print("testcase01")
          self.assertEqual(1,1,"判断相等") #断言2个值相等
          #self.assertIn('h','this')
class demo01(unittest.TestCase):
      def test_demo01_case0(self):
          print("test_demo01_case0")
      def test_demo01_case1(self):
          print("test_demo01_case1")


class demo02(unittest.TestCase):
    def test_demo02_case0(self):
        print("test_demo02_case0")

    def test_demo02_case1(self):
        print("test_demo02_case1")

if __name__=='__main__':
    #unittest.main()
    #suit=unittest.TestSuite()
    #suit.addTest(demo("test_case01"))
    #suit.addTest(demo01("test_demo01_case0"))
    #unittest.TextTestRunner().run(suit)

   # suite=unittest.TestLoader().loadTestsFromTestCase(demo)
    #suite1=unittest.TestLoader().loadTestsFromTestCase(demo01)
    #suiteall=unittest.TestSuite([suite,suite1])
    #unittest.TextTestRunner().run(suiteall)
    discover=unittest.defaultTestLoader.discover("./",'test*.py')
    unittest.TextTestRunner().run(discover)

