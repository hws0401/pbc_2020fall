# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:56:10 2020

@author: Ruby
"""

num = input()

if int(num) == 6174:
    print(num)
else:
    while int(num) != 6174:
        big = ''.join(sorted(num, reverse=True))
        small = ''.join(sorted(num))

        big = int(big)
        small = int(small)

        if big < 1000 and big >= 100:
            big *= 10
        elif big < 100 and big >= 10:
            big *= 100
        elif big < 10 and big >= 1:
            big *= 1000
        else:
            pass

        num = big - small
        num = str(num)

        if int(num) == 6174:
            print(num)
        else:
            print(num, end=',')
