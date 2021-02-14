# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:52:39 2020

@author: Ruby
"""

adult = int(input())
adult_p = int(input())
student = int(input())
student_p = int(input())
bill = int(input())
limit = int(input())
ticket_p = (adult*adult_p) + (student*student_p)
change = bill - ticket_p
remain = 0


if adult + student > limit:
    if change >= 0:
        print('$' + str(change))
if adult + student <= limit:
    if change < 0:
        remain = limit - (adult + student)
        print(str(remain) + ',')
if adult + student <= limit:
    if change >= 0:
        remain = limit - (adult + student)
        print(str(remain) + ',' + '$' + str(change))
