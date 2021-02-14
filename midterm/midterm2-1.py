# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:14:51 2020

@author: Ruby
"""

llist = []

while True:
    xylist = input().split(',')
    if xylist[0] == 'LINESTOP':
        break
    else:
        llist.append(xylist)

for x in llist:
    for y in range(len(x)):
        x[y] = float(x[y])

param = input().split(',')
horvv = param[0]
line = float(param[1])

def plotmirror(linelist, horv='h', loc=0):
    if horv == 'v':
        for i in linelist:
            i[0] -= i[0]*2
            i[0] += loc*2
            i[2] -= i[2]*2
            i[2] += loc*2
    else:
        for i in linelist:
            i[1] -= i[1]*2
            i[1] += loc*2
            i[3] -=i[3]*2
            i[3] += loc*2
    
    afigure = linelist

    return afigure

def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % 
              (i, aline[0], aline[1], aline[2], aline[3]))

plotmirror(llist, horvv, line)
printlines(llist)