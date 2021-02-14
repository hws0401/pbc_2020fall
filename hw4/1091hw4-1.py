# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 18:28:48 2020

@author: Ruby
"""

constraint = input().split(',')
item_n = int(constraint[0])
limit = int(constraint[1])
weight = input().split(',')
weight = [int(i) for i in weight]
utility = input().split(',')
utility = [int(i) for i in utility]
bring = input().split(',')
bring = [int(i) for i in bring]

bring_index = []
weight1 = []
utility1 = []
total_weight = 0
total_utility = 0

# 找出要帶物品的index
for i in range(len(bring)):
    if bring[i] == 1:
        bring_index.append(i)

# 把要帶物品的重量獨立出來
for j in range(len(bring_index)):
    weight1.append(weight[bring_index[j]])

# 把要帶物品的效用獨立出來
for n in range(len(bring_index)):
    utility1.append(utility[bring_index[n]])

# 計算重量和效用總和
for w in weight1:
    total_weight += w
for u in utility1:
    total_utility += u

# 判斷重量是否超出上限
if total_weight <= limit:
    print(str(total_weight) + ',' + str(total_utility))
else:
    print('-1')
