'''
Created on 2017年10月16日

@author: Jorble
'''
import time
import os
import common.exceldata as f
import sys

#默认列名
DEFAULT_COLNAMES = ["用例名称","测试项","测试结果","备注"]

#默认路径为上级工作目录下的results目录
path = os.path.abspath(os.path.join(os.path.join(os.getcwd(), ".."),'results'))
filename = "testResult" +time.strftime("%Y-%m-%d-%H-%M", time.localtime())+".xlsx"

file = os.path.join(path,filename)

#每个测试模块最后返回测试的结果记录，写入excel文件。返回格式为：测试项，测试结果（fail或pass），备注说明
def take_result_record(data=0,init=0,colnames=None):   
    #初始化创建结果记录文件    
    if init != 0:
        #print("new file")
        
        global file
        file = os.path.join(path,filename)
        if not os.path.exists(path):
            os.makedirs(path)
        #file = path + filename
        if colnames == None:
            colnames = DEFAULT_COLNAMES
        f.new_excel(file,colnames)  
    else:
        if not os.path.exists(file):
            if colnames == None:
                colnames = DEFAULT_COLNAMES
            f.new_excel(file,colnames)
           
    #将测试结果写入excel表格中记录
    if data != 0:    
        #print("write excel")
        f.excel_append_row(file,data) 
    elif init == 0:         
        f.excel_append_row(file,"没有数据可写入！") 
        