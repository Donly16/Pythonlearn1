'''
Created on 2017年9月6日
 Jorble
'''

import unittest
import HTMLTestRunner
import time
import os
from common.method import excuteAdbShell
from common import resultFile
from common import exceldata as f
#引入测试用例文件
import testCaseClasses
import Params

DATAFILE = Params.Data_File
#从excel中读取要执行测试的测试类的名字
runcases = f.excel_read_col(DATAFILE,by_name="run",col_name="ClassNames")

#建立测试用例的套集
testunit = unittest.TestSuite()
#添加测试用例
for case in runcases:
    if len(case) > 0:
        className = getattr(testCaseClasses,case)
        testunit.addTest(unittest.makeSuite(className))

#获取上级目录路径
backDir = os.path.abspath(os.path.join(os.getcwd(), ".."))
#拼接结果文件保存目录为当前目录的同级目录
reportFpath = os.path.join(backDir,'results')
reportPath = os.path.join(reportFpath,time.strftime("%Y-%m-%d-%H-%M", time.localtime()))

#判断是否目录存在，不能存在则创建
if not os.path.exists(reportPath):
    os.makedirs(reportPath)

#初始化结果文件
resultFile.path = reportPath
resultFile.filename =  "testResult.xlsx"
resultFile.take_result_record(init = 1)

#指定测试报告保存文件
reportFile = os.path.join(reportPath,'testreport.html')

#以二进制文件打开报告文件，必须以二进制打开，因为报告里面是通过二进制写入的，不然会报错
with open(reportFile,'wb') as fp:
    #print("file opened!")
    #建立runner，写入标题名称和描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='沙龙登录测试报告',description='用例执行情况')
    #运行测试套集
    print("test start!")
    runner.run(testunit)
print("test end")
