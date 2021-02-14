# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:49:27 2020

@author: Ruby
"""

calculate = input()
calist = []
for i in calculate:
    calist.append(i)

for i in range(len(calist)):
    if calist[i] == '+':
        calist[i] = '加'
    elif calist[i] == '-':
        calist[i] = '減'
    elif calist[i] == '/':
        calist[i] = '除以'
    elif calist[i] == '*':
        calist[i] = '乘以'
    elif calist[i] == '=':
        calist[i] = '等於'
    else:
        if calist[i] == '1':
            calist[i] = '一'
        elif calist[i] == '2':
            calist[i] = '二'
        elif calist[i] == '3':
            calist[i] = '三'
        elif calist[i] == '4':
            calist[i] = '四'
        elif calist[i] == '5':
            calist[i] = '五'
        elif calist[i] == '6':
            calist[i] = '六'
        elif calist[i] == '7':
            calist[i] = '七'
        elif calist[i] == '8':
            calist[i] = '八'
        elif calist[i] == '9':
            calist[i] = '九'
        elif calist[i] == '0':
            calist[i] = '零'


zhnum = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '零']
for i in range(len(calist)):
    if i == len(calist)-1:
        pass
    else:
        if (calist[i] in zhnum) and (calist[i+1] in zhnum):
            if calist[i] == '一':
                calist[i] = '十'
                if calist[i+1] == '零':
                    calist[i+1] = ' '
            else:
                calist[i] = calist[i] + '十'
                if calist[i+1] == '零':
                    calist[i+1] = ' '
calist = ''.join(calist)
calist = calist.split(' ')
calist = ''.join(calist)
print(calist)
