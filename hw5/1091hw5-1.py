# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:33:46 2020

@author: Ruby
"""
linelist = []

while True:
    xylist = input().split(',')
    if xylist[0] == 'LINESTOP':
        break
    else:
        linelist.append(xylist)

for x in linelist:
    for y in range(len(x)):
        x[y] = float(x[y])

shiftvalue = input().split(',')
for s in range(len(shiftvalue)):
    shiftvalue[s] = float(shiftvalue[s])


def plotshift(linelist, xshift=0, yshift=0):
    for i in linelist:
        i[0] = i[0] + xshift
        i[2] = i[2] + xshift
        i[1] = i[1] + yshift
        i[3] = i[3] + yshift
    return linelist


def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f"
              % (i, aline[0], aline[1], aline[2], aline[3]))

plotshift(linelist, shiftvalue[0], shiftvalue[1])
printlines(linelist)
