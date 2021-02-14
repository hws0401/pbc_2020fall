# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:19:18 2020

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
rest = 0

# 判斷購買總張數會不會超過上限
if adult + student <= limit:
    rest = limit - (adult + student)
else:
    rest = -1
    
#是否足夠支付票價
if ticket_p <= bill :
    print(str(rest) + ',' + '$' + str(change))
else:
    print(str(rest) + ',' + '-2')