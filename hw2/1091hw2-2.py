# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:49:05 2020

@author: Ruby
"""

kg = int(input())
first_tier = int(input())
ftier_p = int(input())
second_tier = int(input())
stier_p = int(input())
third_tier = int(input())
ttier_p = int(input())
kg_price = 0

if kg > second_tier:
    kg_price = (ftier_p*first_tier) \
                + stier_p*(second_tier - first_tier) \
                + ttier_p*(kg - second_tier)
elif kg <= second_tier and kg > first_tier:
    kg_price = (ftier_p*first_tier) + stier_p*(kg - first_tier)
else:
    kg_price = (ftier_p*kg)

print(kg_price)

