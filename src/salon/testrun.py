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
'''from login import *
from setUrl import *
from creatSalon import *

import setUrl
import creatSalon
import login'''
from salon import testCaseClasses


s = f.excel_read_col("E:\workspace\Pythonlearn1\src\datas.xlsx",by_name="run",col_name="ClassNames")
print("datas:",s)


#建立测试用例的套集
testunit = unittest.TestSuite()
#添加测试用例s
for case in s:
    t = getattr(testCaseClasses,case)
    testunit.addTest(unittest.makeSuite(t))

print(testunit)

