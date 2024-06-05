# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 11:34
# @Author  : 霍格沃兹小学徒

import yaml
def getdata():
    with open('../data/data.yaml','r') as  file:
        content=yaml.safe_load(file)
        return content

def test_addStudent():


