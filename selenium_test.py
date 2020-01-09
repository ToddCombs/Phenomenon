# author:ToddCombs
import time
from selenium import webdriver

def auto_test():

    b = webdriver.Firefox()
    b.get('http://www.dapengjiaoyu.com/')
    b.maximize_window()
    print('当前url为：', b.current_url)
    # print('当前页面源码为：', b.page_source)
    b.find_element_by_link_text('首页').click()
    b.find_element_by_link_text('VIP课').click()
    time.sleep(1)
    b.back()
    b.find_element_by_link_text('公开课').click()
    time.sleep(1)
    b.back()
    b.find_element_by_link_text('帮助中心').click()
    time.sleep(1)
    b.back()
    b.close()

auto_test()


