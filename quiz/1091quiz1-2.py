# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:26:29 2020

@author: Ruby
"""

info = input().split(',')
buy = input().split(',')

bento_q = buy.count('1')
drink_q = buy.count('2')
bnd_q = buy.count('3')

bento_p = int(info[0])
drink_p = int(info[1])
discount = int(info[2])

bento = (bento_q*bento_p)
drink = (drink_q*drink_p)
bnd = ((bento_p + drink_p) - discount)*bnd_q
if bnd < 0:
    bnd = 0

total_bento = bento_q + bnd_q
total_drink = drink_q + bnd_q
total_price = bento + drink + bnd

print(str(total_bento) + ',' + str(total_drink) + ',' + str(total_price))