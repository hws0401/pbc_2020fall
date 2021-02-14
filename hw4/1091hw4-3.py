# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:41:17 2020

@author: Ruby
"""

constraint = input().split(',')
item_n = int(constraint[0])
limit = int(constraint[1])
weight = input().split(',')
weight = [int(i) for i in weight]
utility = input().split(',')
utility = [int(i) for i in utility]

'''
以下是第一種演算法
'''
# 計算物品CP值
cp = []
for i in range(len(utility)):
    cp.append(utility[i]/weight[i])

# 照CP值排序
cp_sorted = sorted(cp, reverse=True)

# 照CP值大小順序找出對應物品的編號
# 相同CP值的放在同一個list內
itemnum = []
samenum = []
for j in cp_sorted:
    for k in range(len(cp)):
        if j == cp[k]:
            samenum.append(k)
            cp.remove(cp[k])
            cp.insert(k, 0)
    itemnum.append(samenum)
    samenum = []

# 考慮重量一樣
# 把小list照重量排序
biglist = []
for m in itemnum:
    newlist = []
    for n in m:
        for w in range(len(weight)):
            if n == w:
                newlist.append(weight[w])
    newlist = sorted(newlist)
    biglist.append(newlist)

# 把重量照cp值對應的編號順序排列
itembyweight = []
for b in biglist:
    for s in b:
        itembyweight.append(s)

# 避免選取到相同重量不同編號的物品
# 選到的物品重量歸零選到的物品重量歸零
eliminate_list = []
for w in range(len(weight)):
    eliminate_list.append(weight[w])

# 按照重量決定選取物品
bringitem = []
totalweight = 0
for l in itembyweight:
    if (totalweight + l) <= limit:
        totalweight += l
        bringitem.append(eliminate_list.index(l)+1)
        eliminate_list.insert(eliminate_list.index(l), 0)
        eliminate_list.remove(l)
    else:
        pass

# 第一種演算法結果
bringitem = sorted(bringitem)


'''
第二種算法
'''
# 將物品照效用排序
utility_sorted = sorted(utility, reverse=True)

# append過的不能再append
# 照效用大小找出對應物品的編號
itemnum2 = []
for p in utility_sorted:
    for q in range(len(utility)):
        if p == utility[q]:
            itemnum2.append(q)

# 判斷重量是否能攜帶
bringitem2 = []
totalweight2 = 0
for r in itemnum2:
    if (totalweight2 + weight[r]) <= limit:
        totalweight2 += weight[r]
        bringitem2.append(r+1)
    else:
        pass

# 第二種演算法結果
bringitem2 = sorted(bringitem2)

utility1 = 0
utility2 = 0
# 比較哪一種演算法效用更大
for ii in bringitem:
    utility1 += utility[ii-1]
for iii in bringitem2:
    utility2 += utility[iii-1]

if utility1 > utility2:
    print(*bringitem, sep=',')
else:
    print(*bringitem2, sep=',')
