# author:ToddCombs
# appium例子1——打开手机计算器输入2019
# 在手机上打开需要获取包名和活动名的app
# 在cmd中运行‘adb shell’命令，进入shell命令行
# 在shell命令行运行dumpsys window windows | grep -E ‘mCurrentFocus’命令获取appPackage和appActivity
import time
from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'Y9CAAMGMD6S8PFAQ'
# desired_caps['platformVersion'] = '6.0'
# desired_caps['deviceName'] = '9HQ4C19909000574'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
# 大鹏教育的appPackage名和首页引导图的Activity
# desired_caps['appPackage'] = 'com.power.dapengeducation'
# desired_caps['appActivity'] = '.ui.login.TransitionActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_name("2").click()
driver.find_element_by_name("0").click()
driver.find_element_by_name("1").click()
driver.find_element_by_name("9").click()
driver.quit()