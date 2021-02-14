# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:19:55 2020

@author: Ruby
"""

pm = int(input())
temp = int(input())
dewpoint = int(input())
threshold = float(input())
pm_will = 0
humidity_will = 0
final_will = 0

#計算PM2.5對意願的影響
if pm <= 35:
    pm_will = 0.5 + (100 - pm)*0.05
else:
    pm_will = 0.5 + (45 - pm)*0.02

#計算濕度對意願的影響
humidity = 100 - 5*(temp - dewpoint)
if humidity <= 30:
    humidity_will = (0.5/60)*(110 - humidity)
else:
    humidity_will = (0.5/45)*(90 - humidity)

#整理PM意願數值
if pm_will < 0:
    pm_will = 0
if pm_will > 1:
    pm_will = 1

#整理濕度意願數值
if humidity_will <0:
    humidity_will = 0
if humidity_will > 1:
    humidity_will = 1

#選擇較低的意願數值
if pm_will <= humidity_will:
    final_will = pm_will
    print('{:.2f}'.format(pm_will))
else:
    final_will = humidity_will
    print('{:.2f}'.format(humidity_will))

#決定要不要跟他約會
if final_will < threshold:
    print('I wouldn\'t go out with you.')
else:
    print('Let\'s go together.')

    