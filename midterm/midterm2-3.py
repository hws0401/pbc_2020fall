# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:42:39 2020

@author: Ruby
"""

fn0 = input()
keyword = input()
fh0 = open(fn0, 'r', encoding='cp950')

for adata in fh0:
    adata = adata.strip('\n')
    ddatta = adata.split(',')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

outputdata = dict()
if keyword == 'TYPE':
    for data in ddatta:
        if is_number(data) == True:
            outputdata[ddatta.index(data)] = 'numerical'
        else:
            outputdata[ddatta.index(data)] = 'categorical'
elif keyword == 'MAXLEN':
    for data in ddatta:
        outputdata[ddatta.index(data)] = len(data)
elif keyword == 'MAXNUMLEN':
    for data in ddatta:
        if (float(data) == False):
            outputdata[ddatta.index(data)] = 0
        else:
            if (float(data)//10) > 1:
                outputdata[ddatta.index(data)] = len(data)
            else:
                outputdata[ddatta.index(data)] = 1
else: #MAXDECPLACE'
    for data in ddatta:
        decplace = data.find('.')
        if decplace == -1:
            outputdata[ddatta.index(data)] = 0
        else:
            dec = data[decplace:]
            outputdata[ddatta.index(data)] = len(dec)

for data in outputdata:
    print('{} : {}'.format(data, outputdata[data]))
