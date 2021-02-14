# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:34:33 2020

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

n = 0  # 需求量落點位置
mini = 99999
mini_kg = 0

while kg <= tier_kg[-1]:
    total = 0
    # 落在x tier以內
    for x in range(len(tier_kg)):
        if tier_kg[x] >= kg:
            n = x
            break

    # 算出需求公斤數相對應價錢
    if n == 0:  # 需求小於第一層級
        total = (kg * tier_price[n])
    else:
        total += ((kg - tier_kg[n-1]) * tier_price[n]) \
                + (tier_kg[0] * tier_price[0])
        while n > 1:
            total += (tier_kg[n-1] - tier_kg[n-2]) * tier_price[n-1]
            n -= 1

    if total <= mini:
        mini = total
        mini_kg = kg

    kg += 1

print(str(mini_kg) + ',' + str(mini))
