# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:27:03 2020

@author: Ruby
"""
# 讀入球賽資料
recordlist = []
while True:
    xylist = input().split(',')
    if xylist[0] == 'RECORDSTOP':
        break
    else:
        recordlist.append(xylist)

# 讀入計算需求
calcneeds = []
while True:
    calclist = input().split(' ')
    if calclist[0] == 'FUNCTIONSTOP':
        break
    else:
        calcneeds.append(calclist)

for r in recordlist:
    r[1] = int(r[1])
    r[2] = int(r[2])
    r[3] = int(r[3])
    r[4] = int(r[4])

for c in calcneeds:
    if c[0] == '1':
        c[2] = int(c[2])
    c[1] = c[1].split(',')
    for cc in range(len(c[1])):
        c[1][cc] = int(c[1][cc])


def chop(avg):
    avg = int(avg*100) / 100
    return avg if avg > 0 else 0


def player_avg(seasons, records, player_number):
    playerinfo = []
    hitrate = 0
    hitnum = 0
    safenum = 0
    # 抓出選定選手的資料
    for r in records:
        if r[1] == player_number and (r[2] in seasons):
            playerinfo.append(r)
    # 找出所需年份對應的數據
    for p in playerinfo:
        hitnum += p[3]
        safenum += p[4]
    hitrate = safenum/hitnum
    print(chop(hitrate))


def team_avg(seasons, records, team_name):
    teaminfo = []
    hitrate = 0
    hitnum = 0
    safenum = 0
    # 抓出選定隊伍的資料
    for r in records:
        if r[0] == team_name and (r[2] in seasons):
            teaminfo.append(r)
    # 找出所需年份對應的數據
    for t in teaminfo:
        hitnum += t[3]
        safenum += t[4]
    hitrate = safenum/hitnum
    print(chop(hitrate))


def best_player(seasons, records):
    targetseason = []
    totalyrate = []
    finaloutput = []
    for s in range(len(seasons)):
        seasons[s] = int(seasons[s])
    # 抓出指定賽季
    for r in records:
        for s in seasons:
            if r[2] == s:
                targetseason.append(r)
    # 計算賽季中球員打擊率
    for s in seasons:
        yearrate = []
        for t in targetseason:
            if t[2] == s:
                hitrate = t[4]/t[3]
                yearrate.append(t[1])
                yearrate.append(hitrate)
        totalyrate.append(yearrate)
    # 賽季內表現比較
    for t in totalyrate:
        maxi = 0
        maxplayer = 0
        for tt in range(1, len(t), 2):
            if t[tt] > maxi:
                maxi = t[tt]
                maxplayer = t[tt-1]
        finaloutput.append(maxplayer)
    print(*finaloutput, sep=',')


def best_team(seasons, records):
    targetseason = []
    totalyrate = []
    finaloutput = []
    for s in range(len(seasons)):
        seasons[s] = int(seasons[s])
    # 抓出指定賽季
    for r in records:
        for s in seasons:
            if r[2] == s:
                targetseason.append(r)
    # 計算賽季中球員打擊率
    for s in seasons:
        yearrate = []
        for t in targetseason:
            if t[2] == s and t[4] != 0:
                hitrate = t[4]/t[3]
                yearrate.append(t[0])
                yearrate.append(hitrate)
        totalyrate.append(yearrate)
    # 賽季內表現比較
    for t in totalyrate:
        maxteam = 0
        maxi = 0
        for tt in range(1, len(t), 2):
            if t[tt] > maxi:
                maxi = t[tt]
                maxteam = t[tt-1]
        finaloutput.append(maxteam)
    print(*finaloutput, sep=',')

for c in calcneeds:
    if c[0] == '1':
        player_avg(c[1], recordlist, c[2])
    elif c[0] == '2':
        team_avg(c[1], recordlist, c[2])
    elif c[0] == '3':
        best_player(c[1], recordlist)
    else:
        best_team(c[1], recordlist)
