# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 11:34
# @Author  : 霍格沃兹小学徒

import yaml
def getdata():
    with open('../data/data1.yaml','r') as  file:
        content=yaml.safe_load(file)
        return content

def writedata():
    list1=[['s01','cindy',20,'female'],['s01','cindy',20,'female']]
    with open('../data/data1.yaml','w') as file:
        yaml.safe_dump(list1,file)
        print(" 输出成功")

def test_addStudent():
    writedata()
    print(getdata())

if __name__ == '__main__':
    writedata()

