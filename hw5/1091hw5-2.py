# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:14:16 2020

@author: Ruby
"""
import math
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

rotatedegree = float(input())


def rotate(linelist, degree=90):
    degree = math.radians(degree)
    for i in linelist:
        originalx = i[0]
        i[0] = (originalx*(math.cos(degree))) - (i[1]*(math.sin(degree)))
        i[1] = (originalx*(math.sin(degree))) + (i[1]*(math.cos(degree)))
        originalx = i[2]
        i[2] = (originalx*(math.cos(degree))) - (i[3]*(math.sin(degree)))
        i[3] = (originalx*(math.sin(degree))) + (i[3]*(math.cos(degree)))
    return linelist


def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f"
              % (i, aline[0], aline[1], aline[2], aline[3]))


rotate(linelist, rotatedegree)
printlines(linelist)
