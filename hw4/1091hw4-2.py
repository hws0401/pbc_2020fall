# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:27:09 2020

@author: Ruby
"""

constraint = input().split(',')
item_n = int(constraint[0])
limit = int(constraint[1])
weight = input().split(',')
weight = [int(i) for i in weight]
utility = input().split(',')
utility = [int(i) for i in utility]

# 計算物品CP值
cp = []
for i in range(len(utility)):
    cp.append(utility[i]/weight[i])

# 照CP值排序
cp_sorted = sorted(cp, reverse=True)

# 照CP值大小順序找出對應物品的編號
itemnum = []
for j in cp_sorted:
    for k in range(len(cp)):
        if j == cp[k]:
            itemnum.append(k)

# 判斷重量是否能夠攜帶
bringitem = []
totalweight = 0
for m in itemnum:
    if (totalweight + weight[m]) <= limit:
        totalweight += weight[m]
        bringitem.append(m+1)
    else:
        pass

bringitem = sorted(bringitem)
print(*bringitem, sep=',')
