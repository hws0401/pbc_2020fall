# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:41:50 2021

@author: Ruby
"""

param = input().split(',')
a = int(param[0])
b = float(param[1])
c1 = int(param[2])
c2 = int(param[3])
n = int(param[4])

# 第一回合
p2 = 0
p1 = ((a+(b*p2)+c1))/2
p2 = ((a+(b*p1)+c2))/2

# 後面的回合
while n > 0:
    print(p1,p2)
    p1 = ((a+(b*p2)+c1))/2
    p2 = ((a+(b*p1)+c2))/2
    n -= 1

print("%0.2f %0.2f" % (p1, p2))