# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:43:51 2020

@author: Ruby
"""

adult = int(input())
adult_p = int(input())
student = int(input())
student_p = int(input())
bill = int(input())
ticket_p = (adult*adult_p) + (student*student_p)
change = bill - ticket_p

if change >= 0: 
    print('$' + str(change))
else:
    print('-1')

