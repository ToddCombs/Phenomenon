# author:ToddCombs
# appium例子2打开大鹏教育
from appium import webdriver
from selenium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '9HQ4C19909000574'
desired_caps['platformVersion'] = '8.1.0'
# desired_caps['deviceName'] = 'Y9CAAMGMD6S8PFAQ'
desired_caps['appPackage'] = 'com.power.dapengeducation'
desired_caps['appActivity'] = '.ui.login.TransitionActivity'
# 大鹏教育的appPackage名和首页引导图的Activity
# desired_caps['appPackage'] = 'com.power.dapengeducation'
# desired_caps['appActivity'] = '.ui.login.TransitionActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)

def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
#屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)    #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipeUp(x1, y1, x1, y2,t)

driver.find_element_by_id("美术")[0].click()
driver.quit()