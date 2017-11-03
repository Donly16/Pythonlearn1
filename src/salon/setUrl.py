'''
Created on 2017年10月13日

@author: Jorble
'''
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
from common import resultFile
from common.resultFile import  take_result_record

import Params 
from common.method import click_by_text

DATAFILE = Params.Data_File
SHEETNAME = "setUrl"

class salonSetUrl(unittest.TestCase):
    
    global userdata
    userdata = method.ExcelTestDataInit(DATAFILE,SHEETNAME)
    
    
    def setUp(self):
        print("urlsetup begin")
        
        desired_caps = Params.desired_caps.copy()        
        desired_caps['noReset'] = False

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
        print("setup over!")
  
    
    def tearDown(self):  
        driver = self.driver          
        print("teardown")

        driver.quit()
    #配置域名
    

    def SetUrlTest(self,caseName):        
        driver = self.driver
        
        data=[caseName,"域名设置"]
        url = userdata[caseName]['url']
        expected = userdata[caseName]['Expected']
        
        name = caseName +'.png'
        picname = os.path.join(resultFile.path,name)
        
        #点击底部“个人”按钮
        method.click_by_id(driver,"personal")
        #点击设置按钮
        method.click_by_id(driver,"setting")
        #点击配置域名
        method.click_by_id(driver,"yulay")
        elem = method.find_by_id(driver,"edit")
        old_url = elem.get_attribute('text')
        if url == old_url:
            r_flag = "Pass"            
            r_data = "域名已经是：{}，无需修改".format(url)
            method.click_by_id(driver,"barimage")#按返回键
        else:            
            #清空原有域名，重新设置新域名
            method.set_value_by_id(driver,"edit",url,clearflag = 1)
            elem = method.find_by_id(driver,"edit")
            new_url = elem.get_attribute('text')
            #点击提交按钮
            method.click_by_text(driver,"提交")
            driver.get_screenshot_as_file(picname) 
            
            try:
                driver.switch_to_alert()            
                if method.click_by_text(driver,"稍后更新"):
                    print("发现新版本，但是稍后再进行更新")
            except:
                print("no new version found")
            
            #提交之后，正确情况应返回设置页面，查找“配置域名”按钮
            elm = method.find_by_id(driver,"yulay")
            
            if elm != 0:
                r_flag = "Pass" if expected == "Pass" else "Fail"            
                r_data = "域名已被成功设置为：{}".format(new_url)
            else:
                r_flag = "Pass" if expected == "Fail" else "Fail"  
                r_data = "域名设置提交失败。当前域名为：{}".format(new_url)  
                method.click_by_id(driver,"barimage")#按返回键
                          
        method.click_by_id(driver,"barimage")#按返回键，回到个人页面
   
        data.append(r_flag)
        data.append(r_data)
        take_result_record(data)
        self.assertIs(r_flag, "Pass")
        return 
    
    @unittest.skipIf(userdata['test_a_seturl']['SkipFlag']=="skip", "用户设置跳过该用例")     
    def test_a_seturl(self):
        caseName = method.get_curfunc_name()
        self.SetUrlTest(caseName)
        return
    

        