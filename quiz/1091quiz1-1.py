# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:23:08 2020

@author: Ruby
"""

bento = int(input())
drink = int(input())
discount = int(input())
price = 0

price = (bento + drink) - discount

if price < 0:
    price = 0
else: pass

print(price)