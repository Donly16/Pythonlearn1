'''
Created on 2017年10月16日

@author: Jorble
'''
import time
import os
import common.exceldata as f

DEFAULT_COLNAMES = ["测试项","测试结果","备注"]
#默认路径为上级工作目录
DEFAULT_PATH = os.path.abspath(os.path.join(os.getcwd(), ".."))
DEFAULT_FILENAME = "testResult" +time.strftime("%Y-%m-%d-%H-%M", time.localtime())+".xlsx"


class ResultFile():
    '''
    classdocs
    '''
    
    path = DEFAULT_PATH
    filename = DEFAULT_FILENAME
    
    file = os.path.join(path,filename)

    def __init__(self, path,filename,colnames = None):
        '''
        Constructor
        '''
        
        file = os.path.join(path,filename)
        if colnames == None:
            colnames = DEFAULT_COLNAMES
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        f.new_excel(file,colnames)
        
    #每个测试模块最后返回测试的结果记录，写入excel文件。返回格式为：测试项，测试结果（fail或pass），备注说明
    def take_result_record(self,data=0):    
        #将测试结果写入excel表格中记录
        if data != 0:    
            #print("write excel")
            f.excel_append_row(file,data) 