'''
Created on 2017年9月6日
 Jorble
'''
import unittest
#import HTMLTestRunner
import HtmlTestRunner 
from login import *
#建立上面测试用例的套集
testunit = unittest.TestSuite()
#添加测试用例，注意格式
testunit.addTest(unittest.makeSuite(salonLogin))

#指定测试报告保存文件
filename = 'E:\\research\\result\\testreport2.html'
#以二进制文件打开报告文件，必须以二进制打开，因为报告里面是通过二进制写入的，不然会报错
fp = open(filename,'w')
print("file opened!")
#建立runner，写入标题名称和描述
#runner = HtmlTestRunner.HTMLTestRunner(stream=fp,report_title='沙龙登录测试报告2',output='用例执行情况')
runner = HtmlTestRunner.HTMLTestRunner(report_title='沙龙登录测试报告2',output='用例执行情况')
    #运行测试套集
print("test start!")
runner.run(testunit)
#关闭文件句柄
fp.close()
print("test end")
