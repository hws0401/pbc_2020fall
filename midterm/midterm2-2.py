# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:45:42 2020

@author: Ruby
"""

stringlist = []

while True:
    string = input()
    if string == 'INPUTSTOP':
        break
    else:
        string = string.strip()
        stringlist.append(string)

sidxlist = []
for string in stringlist:
    sidx = []
    sindex = string.find('\"')
    stmp = string
    while sindex != -1:
        sidx.append(sindex)
        stmp = stmp.replace('\"', '*', 1)
        sindex = stmp.find('\"')
    sidxlist.append(sidx)

for s in range(len(sidxlist)):
    times = len(sidxlist[s])//2
    while times > 0:
            stringlist[s] = stringlist[s].replace('\"', '「', 1)
            stringlist[s] = stringlist[s].replace('\"', '」', 1)
            times -= 1
print(stringlist)

spacelist = []
for string in stringlist:
    ssp = []
    space = string.find(' ')
    stmp = string
    while space != -1:
        ssp.append(space)
        stmp = stmp.replace(' ', '*', 1)
        space = stmp.find(' ')
    spacelist.append(ssp)

for s in range(len(spacelist)):
    spacelen = 1
    if s != -1:
        if spacelist[s+1] = spacelist[s] + 1:
            spacelen += 1
        

