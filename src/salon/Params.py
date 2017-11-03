'''
Created on 2017年10月23日

@author: cyp
'''

Data_File = "E:\workspace\Pythonlearn1\src\datas.xlsx"

desired_caps = {}
desired_caps['platformName'] = 'Android'
#desired_caps['deviceName'] = 'Android_SDK_built_for_x86'#'Android Emulator'
#desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'HONOR H30-L01M'         
desired_caps['platformVersion'] = '6.0'
desired_caps['app'] = 'E:\\apk\\app-release.apk'#被测试的App在电脑上的位置

#desired_caps['appPackage'] = 'com.shalong.fro_soft.shalongapp'
#desired_caps['appActivity'] = 'com.fro.shalong.view.shalong.MainActivity'
desired_caps['noReset'] = True#无需每次都重新安装apk

desired_caps['automationName'] = 'uiautomator2'#用xpath查找'selendroid'#
#无法与安卓6.0兼容
#desired_caps['recreateChromeDriverSessions'] = True

desired_caps['unicodeKeyboard'] = True #设置使用appium的Unicode键盘
desired_caps['resetKeyboard']=True
