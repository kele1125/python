# -*- coding: utf-8 -*-
# @Time    : 2024/7/5 18:48
# @Author  : 霍格沃兹小学徒
from time import sleep
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By

import os

def test_debug1():
    print(os.environ['PATH'])


def test_senlenium():
    service = Service('/Users/liuhua/personal/tools/chromedriver')
    driver=webdriver.Chrome(service=service)
    driver.get('https://www.baidu.com/')
    sleep(3)
    driver.find_element(By.ID,'kw').send_keys('霍格沃兹测试开发学社')
    sleep(3)
    driver.find_element(By.ID,'su').click()
    sleep(3)
    driver.quit()
