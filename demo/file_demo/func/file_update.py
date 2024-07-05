# -*- coding: utf-8 -*-
# @Time    : 2024/6/6 14:27
# @Author  : 霍格沃兹小学徒

import pandas as pd

def getdata():
    refund=pd.read_excel('../data/refund.xlsx',engine='openpyxl')
    invoice = pd.read_excel('../data/invoice.xlsx',engine='openpyxl')
    print(invoice)

def modifydata():
    refund=pd.read_excel('../data/refund.xlsx',engine='openpyxl')
    invoice = pd.read_excel('../data/invoice.xlsx',engine='openpyxl')
    print("Refund DataFrame Columns:", refund.columns)
    print("Refund DataFrame Columns:", invoice.columns)
    invoice_order=set(invoice['商户订单号'])
    print(invoice_order)
    print(refund['商户订单号'])
    refund['会务退款备注']=refund['商户订单号'].apply(lambda order: '已开票' if order in invoice_order else '未开票')
    refund.to_excel(('../data/修改后的退费管理表.xlsx'))

if __name__ == '__main__':
    modifydata()

