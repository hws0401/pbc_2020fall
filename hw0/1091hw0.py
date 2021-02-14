# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:03:15 2020

@author: Ruby
"""

adult = int(input())
student = int(input())
adult_p = int(input())
student_p = int(input())
bill = int(input())
ticket_p = (adult*adult_p) + (student*student_p)
change = bill - ticket_p

print(str(bill) + ',' + str(ticket_p) + ',' + str(change))