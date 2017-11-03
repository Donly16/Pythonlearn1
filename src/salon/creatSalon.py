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
from login import login
import Params 
from common.method import click_by_text

DATAFILE = Params.Data_File  
SHEETNAME = "creatSalon"


#PlatformVersion = Params.desired_caps['platformVersion'] #'6.0'

class salonCreat(unittest.TestCase):
    global userdata
    userdata = method.ExcelTestDataInit(DATAFILE,SHEETNAME)

    def setUp(self):
        print("creatsalon setup begin")
        
        self.desired_caps = Params.desired_caps.copy()        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
  
        print("setup over!")
  
    def tearDown(self):  
        driver = self.driver          
        print("teardown")
        driver.quit()
        
    
    def CreatSalonTest(self,caseName):
        driver = self.driver
        data = [caseName,"创建沙龙"]
        
        salon_name = userdata[caseName]['SalonName']
        salon_desc = userdata[caseName]['SalonDesc']
        salon_pic = userdata[caseName]['SalonPic']
        expected = userdata[caseName]['Expected']
        name = caseName +'.png'
        picname = os.path.join(resultFile.path,name)#跟结果文件存放在同一个目录下
        messStr = userdata[caseName]['Message']
        message = './/*[contains(@text,"'+messStr+'")]'

        #点击“首页”按钮
        method.click_by_id(driver,"main")
        #点击创建沙龙
        cflag = method.click_by_id(driver,"barmore")
        if cflag == 0:
            print("没有发现创建沙龙按钮，以tchf老师登录系统")
            funName = sys._getframe().f_code.co_name
            login(driver,"tchf","12345678",funName)
            method.click_by_id(driver,"main")
            method.click_by_id(driver,"barmore")
        #!!!!这里在4.4.2上很不稳定，有的时候能点击到创建按钮，有的时候点击了却并没有点击到。但是却并没有返回错误信息
        #设置沙龙名称
        flag = method.set_value_by_id(driver,"name",salon_name)
        
        if flag == 0:
            #没有设置名称成功，则多是因为根本就没有点击到创建按钮，没有打开创建页面
            r_flag = "Fail"
            r_data = "没有打开创建沙龙的页面"            
        else:
                        
            #点击老师
            method.click_by_id(driver,"terchers")
            
            tchs = WebDriverWait(driver, timeout=10, poll_frequency=0.5)\
                   .until(lambda x: x.find_elements_by_class_name("android.widget.CheckBox"))
            
            print(tchs)
            if len(tchs) > 0:
                tchs[0].click()#点击选择第一个老师
                click_by_text(driver,"确定")

            #点击简介
            #method.click_by_id(driver,"editor")#在6.0上简介的id是editor，但是在4.4.2上却叫detail2
            if len(salon_desc) > 0:
                if self.desired_caps['platformVersion'] == '6.0':
                    method.click_by_id(driver,"editor")
                else:
                    #4.4.2极不稳定啊！有的时候能找到，有的时候找不到！
                    eflag = method.click_by_id(driver,"details")
                    #如果没有找到，就再找一次！！！
                    if eflag == 0:#结果还是找不到！！！！！这是什么情况？
                        method.click_by_classname(driver,"android.webkit.WebView")#通过class名查找简介控件,有的时候能找到，有的时候找不到

                #输入详情内容
                method.set_value_by_classname(driver,"android.widget.ScrollView",salon_desc)
                method.click_by_text(driver,"确定")
            if salon_pic != "no":    
                #设置沙龙图片。首先点击图片按钮
                method.click_by_id(driver,"image")
                time.sleep(10)#等待图片文件夹加载出来
                
                width =  driver.get_window_size()['height'] 
                height =  driver.get_window_size()['width']
                print("屏幕宽度:{},高度:{}".format(width,height))
                y=width//4
                x = height//3
                pos =([x,y],)
                print("点击选择第一个图片文件夹.z 位置:{}".format(pos))
                
                driver.tap(pos)#点击第一个图片文件夹
                print("等待10秒让图片加载完成")
                time.sleep(10)#等待图片加载出来
                print("等待结束，开始点击选择图片")
                
                y=width//4
                x=height//5
                pos =([x,y],)
    
                print("点击选择第一张图片。位置：{}".format(pos))
                driver.tap(pos)#点击第一张图片
                print("等待10秒让图片加载完成")
                time.sleep(10)#等待图片加载
                print("等待结束，开始点击保存图片或者确认图片")
                
                #4.4.2手机上，选择图片后直接进入了裁剪页面，点击确定就保存图片            
                if self.desired_caps['platformVersion'] != '6.0':
                    method.click_by_text(driver,"确定")                
                else:
                    #6.0手机上，点击图片后还有一个确认的动作，然后再是确定保存裁剪图片
                    method.click_by_desc(driver,"确定")
                    method.click_by_desc(driver,"确定")
        
            
    
            method.click_by_text(driver,"确定")#点击确定按钮创建沙龙

            driver.get_screenshot_as_file(picname)  
            toast_text = method.get_toast_text(driver,message)           
            print("toast is ",toast_text)
            elem = method.find_by_text(driver,"确定")#查找确定按钮，如果新建成功，则该按钮不会再可见
            if elem != 0:
                method.click_by_id(driver,"barimage")#按返回键，回到个人页面         
                
                r_flag = "Pass" if expected == "Fail" else "Fail" 
                r_data = "创建沙龙失败。沙龙名称：{}".format(salon_name)               
                                  
            else:
                r_flag = "Pass" if expected == "Pass" else "Fail"  
                r_data = "创建沙龙成功。沙龙名称为：{}".format(salon_name)                
        #测试数据写入报告中
        print(r_data)
        data.append(r_flag)
        data.append(r_data) 
        data.append(toast_text)
        take_result_record(data)   
        
        #将html报告中的用例执行状态置为pass或者fail
        self.assertIs(r_flag,"Pass") 
        return 

    @unittest.skipIf(userdata['test_a_creatSalon']['SkipFlag']=="skip", "用户设置跳过该用例")     
    def test_a_creatSalon(self):
        caseName = method.get_curfunc_name()
        self.CreatSalonTest(caseName)
        return
    
    @unittest.skipIf(userdata['test_b_creatSalon']['SkipFlag']=="skip", "用户设置跳过该用例")     
    def test_b_creatSalon(self):
        caseName = method.get_curfunc_name()
        self.CreatSalonTest(caseName)
        return
    
    @unittest.skipIf(userdata['test_c_creatSalon']['SkipFlag']=="skip", "用户设置跳过该用例")     
    def test_c_creatSalon(self):
        caseName = method.get_curfunc_name()
        self.CreatSalonTest(caseName)
        return
    @unittest.skipIf(userdata['test_d_creatSalon']['SkipFlag']=="skip", "用户设置跳过该用例")     
    def test_d_creatSalon(self):
        caseName = method.get_curfunc_name()
        self.CreatSalonTest(caseName)
        return
    