import unittest
import os
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By
from common import method
import sys
import common.exceldata as f
from unittest.case import skip
from common import resultFile
from common.resultFile import  take_result_record
import Params 

DATAFILE = Params.Data_File 
SHEETNAME = "login"


def login(driver,username,passwd,caseName="login"):
    #driver = self.driver 
    #以调用该方法的函数名来给图片命名
    name = caseName +'.png'
    picname = os.path.join(resultFile.path,name)#跟结果文件存放在同一个目录下
    #点击底部“个人”按钮
    method.click_by_id(driver,"personal")    
    #尝试点击登录        
    loginedFlag = method.click_by_text(driver, "点此登录")
    #如果找不到“点此登录"按钮，则说明当前已经是登录状态，需要先退出登录
    if loginedFlag == 0:
        time.sleep(1)
        method.swipeUp(driver)#向上滑动屏幕，以使“退出登录”按钮可见。
        method.click_by_id(driver, 'logout')            
        driver.switch_to_alert()#将焦点切换到弹出窗口中
        method.click_by_text(driver,'确定')
        method.swipeDown(driver)#向下滑动屏幕，以使“点击登录”按钮可见。            
        #点击“点此登录"，去到登录页面
        method.click_by_id(driver,"username")
    
            
    #清空用户名，然后输入新的用户名
    method.set_value_by_id(driver,"et_username",username,clearflag=1)        
    #输入密码
    method.set_value_by_id(driver,"et_password",passwd)        
    #点击“登录”按钮
    method.click_by_id(driver,"login") 
    driver.get_screenshot_as_file(picname)

class salonLogin(unittest.TestCase):
    
    global userdata
    userdata = method.ExcelTestDataInit(DATAFILE,SHEETNAME)
    
    def setUp(self):
        print("setup begin")        
        
        desired_caps = Params.desired_caps.copy()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        print("setup over!")
  
    def tearDown(self):  
        driver = self.driver          
        print("teardown")        
        driver.quit()
    
    def loginTest(self,caseName):            
        driver = self.driver
        print("login began")
        data=[caseName,"用户登录"]

        username = userdata[caseName]['UserName']#u'tchf'
        passwd = userdata[caseName]['Passwd']#u'12345678''        
        messStr = userdata[caseName]['Message']
        message = './/*[contains(@text,"'+messStr+'")]'
        expected = userdata[caseName]['Expected']
        
        login(driver,username,passwd,caseName)
        
        
        toast_text = method.get_toast_text(driver,message)
        '''
        element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, message)))
        print(element)
        if element:
            toast_text = element.get_attribute("text")            
        else:
            toast_text = "没有找到toast"'''
        print("toast is :"+toast_text)    
        
        elm = method.find_by_id(driver,"personal")

        if elm == 0:
            r_flag = "Pass" if expected == "Fail" else "Fail"
            r_data = "用户({})+密码({}) 登录失败!".format(username,passwd)
            method.click_by_id(driver,"barimage")#按返回键，回到个人页面
            
        else:
            r_flag = "Pass" if expected == "Pass" else "Fail"  
            r_data = "用户({})+密码({}) 登录成功!".format(username,passwd)
            
        print(r_data)   
        #数据写入报告文件中
        data.append(r_flag) 
        data.append(r_data)
        data.append(toast_text)
        take_result_record(data)  
        #将html报告中的用例执行状态置为pass或者fail
        self.assertIs(r_flag,"Pass")  
        #self.assertIn(messStr,toast_text)
    
    @unittest.skipIf(userdata['test_a_login_succ']['SkipFlag']=="skip", "用户设置跳过该用例")     
    def test_a_login_succ(self):
        caseName = method.get_curfunc_name()
        self.loginTest(caseName)  
        
        return 
  
    @unittest.skipIf(userdata['test_b_login_wronguser']['SkipFlag']=="skip", "用户设置跳过该用例")
    def test_b_login_wronguser(self):
        caseName = method.get_curfunc_name()
        self.loginTest(caseName)  
        
        return 
    @unittest.skipIf(userdata['test_c_login_wrongpass']['SkipFlag']=="skip", "用户设置跳过该用例")
    def test_c_login_wrongpass(self):
        caseName = method.get_curfunc_name()
        self.loginTest(caseName)  
        
        return 
    @unittest.skipIf(userdata['test_d_login_emptyuser']['SkipFlag']=="skip", "用户设置跳过该用例")     
    def test_d_login_emptyuser(self):
        caseName = method.get_curfunc_name()
        self.loginTest(caseName)  
        
        return 
    @unittest.skipIf(userdata['test_e_login_emptypass']['SkipFlag']=="skip", "用户设置跳过该用例")
    def test_e_login_emptypass(self):
        caseName = method.get_curfunc_name()
        self.loginTest(caseName)  
        
        return 