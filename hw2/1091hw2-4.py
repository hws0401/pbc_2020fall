# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:45:15 2020

@author: Ruby
"""

days = int(input())
sleep = 0
hr = 0
lemonmask = 0
eggmask = 0
honmask = 0
price = 0

# 算出需要多少檸檬面膜
for i in range(days):
    hr = float(input())
    sleep += hr
    if hr > 7:
        lemonmask += 1
    else:
        pass

# 算出需要多少蛋白或蜜糖面膜
if (sleep/days) > 6:
    eggmask += (days - lemonmask)
else:
    honmask += (days - lemonmask)

# 計算材料價錢
lemonp = 7
almondp = 0.6
honeyp = 1.2
eggp = 25
lemonq = (lemonmask*1.5)
eggq = ((2*eggmask)/3)

if lemonq > int(lemonq):
    lemonq = ((lemonmask*1.5)//1) + 1
else: 
    lemonq = ((lemonmask*1.5)//1)
    
if eggq > int(eggq):
    eggq = (((2*eggmask)/3)//1) + 1
else:
    eggq = (((2*eggmask)/3)//1)


if lemonq >= 5:
    price = ((lemonq*lemonp)*0.9) + ((lemonmask*4)*almondp) \
            + ((honmask*18)*honeyp) + ((honmask*9)*almondp) \
            + (eggq*eggp) + ((6*eggmask)*honeyp)
else:
    price = (lemonq*lemonp) + ((lemonmask*4)*almondp) \
            + ((honmask*18)*honeyp) + ((honmask*9)*almondp) \
            + (eggq*eggp) + ((6*eggmask)*honeyp)

print(int(price))

















