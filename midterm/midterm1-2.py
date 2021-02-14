# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:29:18 2020

@author: Ruby
"""

num = int(input())
xnum = input().split(',')
xnum = [int(i) for i in xnum]
ylist = []

for i in range(len(xnum)-1):
    y = xnum[i] - xnum[i+1]
    if y < 0:
        y = 0
    else:
        pass
    ylist.append(y)

mini = min(ylist)

print(mini)