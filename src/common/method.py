'''
Created on 2017年9月20日

@author: Jorble
'''
import sys
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By
from common import exceldata

from . import exceldata as f
import subprocess

#执行adb命令的函数
#command示例：
#获取默认输入法：command1 ='adb shell settings get secure default_input_method' 
#设置某种输入法：command = "adb shell ime set io.appium.android.ime/.UnicodeIME"
def excuteAdbShell(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return(p.stdout.readlines())


class ElementNotFound(Exception):
    def __init__(self, value):
            self.value = value
    def __str__(self):
        return repr(self.value)
    

def find_by_id(driver,id):
    try:
        elm = WebDriverWait(driver, timeout=20, poll_frequency=0.5).until(lambda x: x.find_element_by_id(id))
    except:
        elm = 0
        print("find_by_id:%s not found.Unexpected error:%s"%(id,sys.exc_info()[0]))
        #raise ElementNotFound("%s not found.Unexpected error:%s"%(id,sys.exc_info()[0]))
    return elm

def find_by_classname(driver,classname):
    try:
        elm = WebDriverWait(driver, timeout=20, poll_frequency=0.5).until(lambda x: x.find_element_by_class_name(classname))
    except:
        elm = 0
        print("find_by_classname:%s not found.Unexpected error:%s"%(classname,sys.exc_info()[0]))
        #raise ElementNotFound("%s not found.Unexpected error:%s"%(id,sys.exc_info()[0]))
    return elm

def find_by_text(driver,text):
    s = 'new UiSelector().text(\"'+ text +'\")'
    try:
        elm = WebDriverWait(driver, timeout=20, poll_frequency=0.5).until(lambda x: x.find_element_by_android_uiautomator(s))
        #elem4=driver.find_element_by_android_uiautomator("new UiSelector().text(\"8\")"); 
    except:
        elm = 0
        print("find_by_text:%s not found.Unexpected error:%s"%(text,sys.exc_info()[0]))
        #raise ElementNotFound("%s not found.Unexpected error:%s"%(id,sys.exc_info()[0]))
    return elm
def find_by_desc(driver,desc):
    try:
        elm = WebDriverWait(driver, timeout=20, poll_frequency=0.5).until(lambda x: x.find_element_by_accessibility_id(desc))
        
    except:
        elm = 0
        print("find_by_desc:%s not found.Unexpected error:%s"%(desc,sys.exc_info()[0]))
        
    return elm

def find_by_xpath(driver,message):
    try:
        elm = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, message)))
    except:
        elm = 0
        print("find_by_xpath:%s not found.Unexpected error:%s"%(message,sys.exc_info()[0]))
    return elm
        

def myclear(driver,element):
    element.click()
    time.sleep(3)#据说等待1秒，是为了保证全选功能的正常运行
    driver.press_keycode(29,28672)#29-键盘A，28672-META_CTRL_MASK
    driver.press_keycode(112)#112-FORWARD_DEL，67也可以

def click_by_id(driver,id):
    element = find_by_id(driver,id)
    if element != 0:
        element.click()
    return element    

def click_by_classname(driver,classname):
    element = find_by_classname(driver,classname)
    if element != 0:
        element.click()
    return element    
def click_by_text(driver,text):
    element = find_by_text(driver,text); 
    if element != 0:
        element.click()
    return element  

def click_by_desc(driver,desc):
    element = find_by_desc(driver,desc); 
    if element != 0:
        element.click()
    return element 

def click_by_xpath(driver,message):
    element = find_by_xpath(driver,message); 
    if element != 0:
        element.click()
    return element

def set_value_by_id(driver,id,value,clearflag=0):
    #element = find_by_id(driver,id)
    element = click_by_id(driver,id)
    flag = False
    if element != 0:
        if clearflag != 0:
            pass
            element.clear()
            #myclear(driver,element)
        #element.set_value(value)#set_value无法发送中文字符
        #element.send_keys(value)
        element.set_text(value)
        #driver.hide_keyboard()
        flag = True    
        print("id-setvalue:",value)
    return element

def set_value_by_classname(driver,classname,value,clearflag=0):
    element = find_by_classname(driver,classname)

    if element != 0:
        if clearflag != 0:
            element.clear()
            #myclear(driver,element)
        #element.set_value(value)
        element.send_keys(value)
   
        print("class-setvalue:",value)
    return element

def get_toast_text(driver,message):
    #element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, message)))
    element = find_by_xpath(driver,message); 
    if element != 0:    
        text = element.get_attribute("text")
    else:
        text="没有找到toast"
    return text

#获得机器屏幕大小x,y
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print("width:",x," height:",y)
    return (x, y)
#屏幕向上滑动
def swipeUp(driver,ms=None):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.8)   #起始y坐标
    y2 = int(l[1] * 0.2)   #终点y坐标
    #print("up:x1=",x1,",y1=",y1,",y2=",y2)
    driver.swipe(x1, y1, x1, y2,ms)
#屏幕向下滑动
def swipeDown(driver,ms=None):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.2)   #起始y坐标
    y2 = int(l[1] * 0.8)   #终点y坐标
    #print("down:x1=",x1,",y1=",y1,",y2=",y2)
    driver.swipe(x1, y1, x1, y2,ms)
#屏幕向左滑动
def swipLeft(driver,ms=None):
    l=getSize(driver)
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,ms)
#屏幕向右滑动
def swipRight(driver,ms=None):
    l=getSize(driver)
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    driver.swipe(x1,y1,x2,y1,ms)

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
    return userdata
    
    
def get_curfunc_name():
    return(sys._getframe().f_back.f_code.co_name)

def get_backfunc_name():
    return(sys._getframe().f_back.f_back.f_code.co_name)