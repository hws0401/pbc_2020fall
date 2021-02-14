# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:28:10 2020

@author: Ruby
"""

need = input().split(',')
pricing = input().split(',')

tier = int(need[0])
kg = int(need[1])

tier_kg = pricing[:len(pricing)//2]
tier_price = pricing[len(pricing)//2:]

# 把list當中的內容轉成int
for i in range(len(tier_kg)):
    tier_kg[i] = int(tier_kg[i])
for j in range(len(tier_price)):
    tier_price[j] = int(tier_price[j])

n = 0  #需求量落點位置
total = 0


# 落在x tier以內
for x in range(len(tier_kg)):
    if tier_kg[x] >= kg:
        n = x
        break

if n == 0:  # 需求小於第一層級
    total = (kg * tier_price[n])
else:
    total += ((kg - tier_kg[n-1]) * tier_price[n]) \
            + (tier_kg[0] * tier_price[0])
    while n > 1:
        total += (tier_kg[n-1] - tier_kg[n-2]) * tier_price[n-1]
        n -= 1

print(total)
