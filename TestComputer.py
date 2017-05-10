import unittest
import HTMLTestRunner
def addnum(num1,num2):
    return num1+num2
class TestComputer(unittest.TestCase):
    def test_should_good_for_negative_number(self):
        self.assertEqual(0,addnum(-1,1))
    def test_should_good_for_bignum_morethan_10000000000(self):
        self.assertEqual(10000000001,addnum(1,10000000000))
    def test_should_good_for_bignegativenum_morethan10000000000(self):
        self.assertEqual(-10000000001,addnum(-1,-10000000000))

if __name__=='__main__':
    # unittest.main()
    HTMLTestRunner.main()