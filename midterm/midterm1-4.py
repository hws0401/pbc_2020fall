# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:00:51 2020

@author: Ruby
"""

distance = input().split(',')
disx = int(distance[0])
disy = int(distance[1])
dis = int(distance[2])
popu = []

for m in range(disy+1):
    p = input().split(',')
    p = [int(i) for i in p]
    popu.append(p)


maxpopu = 0
totalpopu = []
nextpositionx = dis
nextpositiony = dis
for y in range(disy+1):
    for x in range(disx+1):
        sumpopu = []
        for i in range(len(popu)):
            for j in range(len(popu[i])):
                if (abs(i-y) + abs(j-x)) <= dis:
                    sumpopu.append(popu[i][j])
        totalpopu.append(sum(sumpopu))


print(max(totalpopu))
