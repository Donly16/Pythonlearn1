import sys
import common.exceldata as f
from common.resultFile import  take_result_record

def get_cur_info():
    print(sys._getframe().f_code.co_name)
    print(sys._getframe().f_back.f_code.co_name)
    print(sys._getframe().f_back.f_back.f_code.co_name)


def get_back_info():
    get_cur_info()



def ExcelTestDataInit(file,by_name):
    lines = f.excel_read_row(file,by_name=by_name)
    num = len(lines)
    userdata={}
    #将数据重新组装成新的字典，以第一列用例名为字典的key值，后续其他列组成的字典列表为键值
    for i in range(num):        
        casename = lines[i]["CaseName"]
        del lines[i]["CaseName"]
        '''#将读取到的数据转换为字符串
        for key in lines[i].keys():
            nstr = str(lines[i][key])
            lines[i][key] = nstr
       '''
        userdata[casename] = lines[i]
        take_result_record(["test"])
    return userdata

def test():
    d = ExcelTestDataInit("E:\workspace\Pythonlearn1\src\datas.xlsx","login")
    print(d)
    s = d['test_a_login_succ']['SkipFlag']
    print(s)
    get_cur_info()
    print(len(s))

test()

