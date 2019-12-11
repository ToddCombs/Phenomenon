# author:ToddCombs
# appium例子2打开大鹏教育
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '9HQ4C19909000574'
desired_caps['appPackage'] = 'com.power.dapengeducation'
desired_caps['appActivity'] = '.ui.login.TransitionActivity'
# 大鹏教育的appPackage名和首页引导图的Activity
# desired_caps['appPackage'] = 'com.power.dapengeducation'
# desired_caps['appActivity'] = '.ui.login.TransitionActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_elements_by_tag_name("作业").click()
driver.quit()