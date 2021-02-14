# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:59:52 2020

@author: Ruby
"""

constraints = input().split(',')
numof_invest = int(constraints[0])
budget = int(constraints[1])
riskadvert = int(constraints[2])
capital = input().split(',')
for c in range(len(capital)):
    capital[c] = int(capital[c])
returnvalue = input().split(',')
for r in range(len(returnvalue)):
    returnvalue[r] = int(returnvalue[r])
variant_matrix = []
eliminate_list = []

# 變異數矩陣
for a in range(numof_invest):
    variant = input().split(',')
    for v in range(len(variant)):
        variant[v] = int(variant[v])
    variant_matrix.append(variant)

# 只算第一項投資標的
# 找budget比較小
target_invest = []
value_pool = []
for i in range(len(returnvalue)):
    investment_value = returnvalue[i] - (riskadvert*variant_matrix[i][i])
    value_pool.append(investment_value)
max_value = max(value_pool)
max_value_index = value_pool.index(max(value_pool))
# 第一輪選取
for ii in range(len(value_pool)):
    # 報酬一樣而且價錢一樣
    if value_pool[ii] == max_value and capital[ii] == capital[max_value_index]:
        if ii < max_value_index:
            max_value = value_pool[ii]
            max_value_index = ii
    # 報酬一樣但價錢較低
    elif value_pool[ii] == max_value and \
            capital[ii] < capital[max_value_index]:
        max_value = value_pool[ii]
        max_value_index = ii
    # 報酬最大且符合預算
    elif value_pool[ii] > max_value and capital[ii] <= budget:
        max_value = value_pool[ii]
        max_value_index = ii
    else:
        pass
if max_value <= 0:
    pass
else:
    target_invest.append(max_value_index+1)

# 繼續計算續投資，無投資標的則print(0)結束
if len(target_invest) == 0:
    print(0)
else:
    # 第一輪投資後剩餘預算＆移除已選擇投資標的
    budget -= capital[target_invest[0]-1]
    eliminate_list.append(target_invest[0])
    investment_value = 0
    max_value_index = 0
    max_value = -9999
    while max_value != 0:  # 當有可選取的投資標的
        value_pool = []
        for j in range(len(returnvalue)):
            if capital[j] > budget:  # 超過預算不選取
                value_pool.append(0)
            else:
                investment_value = returnvalue[j] \
                                - (riskadvert*variant_matrix[j][j])
                for l in target_invest:  # 根據已選取數量進行loop
                    investment_value -= riskadvert*(variant_matrix[j][l-1] +
                                                    variant_matrix[l-1][j])
                value_pool.append(investment_value)
        max_value = value_pool[0]
        # 第二輪以後的選取判斷
        for k in range(len(value_pool)):
            # 報酬一樣而且價錢一樣
            if value_pool[k] == max_value \
                    and capital[k] == capital[max_value_index]:
                if k < max_value_index:
                    max_value = value_pool[k]
                    max_value_index = k
            # 報酬一樣但價錢較低
            elif value_pool[k] == max_value \
                    and capital[k] < capital[max_value_index]:
                max_value = value_pool[k]
                max_value_index = k
            # 報酬最大且符合預算
            elif value_pool[k] > max_value and capital[k] <= budget:
                max_value = value_pool[k]
                max_value_index = k
            else:
                pass
        # 若有正報酬而且沒被選取過就選擇該投資標的
        if max_value > 0 and max_value_index+1 not in eliminate_list:
            target_invest.append(max_value_index+1)
            budget -= capital[max_value_index]
            eliminate_list.append(max_value_index)
        else:
            max_value = 0
            break

target_invest = sorted(target_invest)
print(*target_invest, sep=',')
