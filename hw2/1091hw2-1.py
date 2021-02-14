# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:16:31 2020

@author: Ruby
"""

num = int(input())
maxi = 0
midi = 0
mini = 0
i = 0

while i < 3:
    hun = int(num // 100)
    tens = int((num % 100) // 10)
    unit = int((num % 10) / 1)

    maxi = hun
    if maxi < tens:
        maxi = tens
    if maxi < unit:
        maxi = unit

    mini = unit
    if mini > hun:
        mini = hun
    if mini > tens:
        mini = tens

    midi = tens
    if hun > mini and hun < maxi:
        midi = hun
    if unit > mini and unit < maxi:
        midi = unit

    big = (maxi*100) + (midi*10) + (mini*1)
    small = (mini*100) + (midi*10) + (maxi*1)
    if big < 10:
        big *= 100
    elif big < 100:
        big *= 10
    else:
        pass

    num = big - small
    if i < 2:
        print(num, end=',')
    else:
        print(num)
    i += 1
