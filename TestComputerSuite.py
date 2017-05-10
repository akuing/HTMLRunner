import unittest
import os
import HTMLTestRunner
from TestComputer import TestComputer

direct = os.getcwd()
class TestComputerSuite(unittest.TestCase):
  def test_Issue(self):

        computer_test = unittest.TestSuite()
        computer_test.addTests([
            TestComputer(methodName="test_should_good_for_negative_number"),
            TestComputer(methodName="test_should_good_for_bignum_morethan_10000000000"),
            TestComputer(methodName="test_should_good_for_bignegativenum_morethan10000000000")
        ])

        outfile = open(direct + "\computerTest.html", "w",encoding="utf-8")

        computerRunner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='测试报告',
            description='Computer Tests'
        )

        computerRunner.run(computer_test)
        outfile.close()


if __name__ == '__main__':
    unittest.main()
