# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:48:44 2020

@author: Ruby
"""

items = int(input())  # 商品種類數
bundle = input().split(',')  #組合內商品編號
price = input().split(',')  # 所有商品價錢
price = [int(i) for i in price]
quantity = input().split(',')  #所需商品數量
quantity = [int(i) for i in quantity]
bundle_q = []  # 組合商品

# 將商品編號轉換成index
for i in range(len(bundle)):
    bundle[i] = int(bundle[i])-1

# 將套組商品放進專屬的list
for j in bundle:
    bundle_q.append(int(quantity[j]))

# 找出套組數量
mini = bundle_q[0]
for q in bundle_q:
    if q < mini:
        mini = q


#算出全部商品原價
original_p = 0
for p in range(len(quantity)):
    original_p += quantity[p] * price[p]

# 商品扣掉套組數量
for x in range(len(bundle_q)):
    bundle_q[x] = bundle_q[x] - mini

for v in range(len(bundle)):
        quantity.remove(quantity[bundle[v]])
        quantity.insert(bundle[v],bundle_q[v])  # 放回扣掉套組數量的商品

totalprice = 0
for m in range(len(quantity)):
    totalprice += quantity[m] * price[m]

bundleprice = 0
for n in range(len(bundle)):
    bundleprice += price[bundle[n]] 

off20 = (mini // 5)*5
off10 = mini % 5

totalprice += (bundleprice * off20 * 0.8) + (bundleprice * off10 * 0.9)
newmember = (original_p - totalprice)//1000

if newmember >= 1:
    print(str(int(totalprice)) + ',' + str(int(newmember)))
else:
    print('So sad. I messed up.')
