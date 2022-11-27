import unittest

class TestClass1(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("*#" * 30)
    #     print("Class 1 -> class level setUp")
    #     print("*#" * 30)

    def setUp(self):
        print("*#" * 30)
        print("Class 1 -> setUp method is ruuning ")
        print("*#" * 30)

    def test_class1_methodA(self):
        print("Running class 1 -> method A")
        self.assertNotEqual('aBc'.upper(), 'XYZ', msg="The string passed are not equal ")

    # def test_class1_methodB(self):
    #     print("Running class 1 -> method B")

    def tearDown(self):
        print("*#" * 30)
        print("Class 1 -> tearDown method is running")
        print("*#" * 30)

    # @classmethod
    # def tearDownClass(cls):
    #     print("*#" * 30)
    #     print("Class 1 -> class level tearDown")
    #     print("*#" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)