# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:09:20 2020

@author: Ruby
"""

tier = int(input())
kg = int(input())
prev_tier = 0
prev_p = 0
now_tier = 0
now_p = 0
total_p = 0


for x in range(tier):
    now_tier = int(input())
    now_p = int(input())
    if kg > now_tier:
        total_p += (now_tier - prev_tier) * now_p
        prev_tier = now_tier
        prev_p = now_p
    else:
        total_p += (kg - prev_tier) * now_p
        break

print(total_p)

    
    
        
    
    

