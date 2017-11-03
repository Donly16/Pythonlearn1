'''
Created on 2017年10月13日

@author: Jorble
'''
from assertpy import assert_that
import unittest
import HTMLTestRunner
import sys
def testsomething():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'x']).contains('a').does_not_contain('x')
  
#testsomething()



class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FoO')
        
    @unittest.skip("skip")
    def test_contain(self):
        self.assertIn("user", "user wrong", "user is not in it")

if __name__ == '__main__':
    #unittest.main()
    #建立测试用例的套集

    testunit = unittest.TestSuite()
    #添加测试用例
    testunit.addTest(unittest.makeSuite(TestStringMethods))
    filename = "E:/testreport.html"
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='沙龙登录测试报告',description='用例执行情况')
        runner.run(testunit)