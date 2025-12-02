import ddt
import  unittest

@ddt.ddt
class test_se(unittest.TestCase):
    def setUp(self):
        pass

    @ddt.data(2,3)
    def test_01(self,tt):
        print(tt)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
