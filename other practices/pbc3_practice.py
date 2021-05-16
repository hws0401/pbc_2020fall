# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:54:29 2021

@author: Ruby
"""
from datetime import datetime

# 讀入檔案
fn0 = input()
timeslot = input().split(' ')
fh0 = open(fn0, 'r', encoding='utf-8')
next(fh0, None)  #跳過第一行表頭不讀
finallist = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

# 把input轉成可比較的datetime格式
timeslot[0] = datetime.strptime(timeslot[0], '%H:%M:%S').time()
timeslot[1] = datetime.strptime(timeslot[1], '%H:%M:%S').time()

class submission:
    def __init__(self, sid, student, prob, stat, score, length, stime):
        self.sid = sid
        self.student = student
        self.prob = prob
        self.stat = stat
        self.score = score
        self.length = length
        self.stime = stime
        
sublist = []
for aline in fh0:
    aline = aline.rstrip()
    aline = aline.split(',')
    aline[0] = int(aline[0])
    aline[1] = int(aline[1])
    aline[2] = int(aline[2])
    aline[3] = str(aline[3])
    aline[4] = int(aline[4])
    aline[5] = int(aline[5])
    aline[6] = datetime.strptime(aline[6], '%H:%M:%S').time()
    subname = aline[0]
    subname = submission(aline[0], aline[1], aline[2], aline[3], aline[4], aline[5], aline[6])
    sublist.append(subname)

target = []  #在時間區間內的繳交
def findsub(subs, timestrt, timeend):
    for ss in subs:
        if (ss.stime > timeslot[0]) and (ss.stime < timeslot[1]):
            target.append(ss)
    for t in target:
        if t.stat == 'Accepted':
            finallist[(t.prob)-1][0] += 1
        elif t.stat == 'Compile Error':
            finallist[(t.prob)-1][1] += 1
        elif t.stat == 'Runtime Error':
            finallist[(t.prob)-1][2] += 1
        elif t.stat == 'Time Limit Exceed':
            finallist[(t.prob)-1][3] += 1
        elif t.stat == 'Wrong Answer':
            finallist[(t.prob)-1][4] += 1
    return finallist

fh0.close()
print(findsub(sublist, timeslot[0], timeslot[1]))