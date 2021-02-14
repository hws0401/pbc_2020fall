# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:42:02 2020

@author: Ruby
"""

constraint = input().split(',')
itemq = int(constraint[0])
limit = int(constraint[1])
itemw = input().split(',')
itemw = [int(i) for i in itemw]
itemw = sorted(itemw, reverse=True)
boxes = 0


if (sum(itemw)%limit) == 0:
    boxes = sum(itemw)//limit
else:
    boxes = (sum(itemw)//limit)+1

print(boxes)