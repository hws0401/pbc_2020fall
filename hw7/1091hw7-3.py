# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:46:35 2020

@author: Ruby
"""
headline = input()  # 新聞標題檔
ndict = input()  # 關鍵字字典檔
compcat = input()  # 公司類別檔
crit = input().split(',')
target = crit[0]  # 目標類股
targetq = int(crit[1])  # 目標購買數量
rquant = crit[2].split(':')  # 張數分配
for r in range(len(rquant)):
    rquant[r] = int(rquant[r])
fh0 = open(headline, 'r', encoding='utf-8')
fh1 = open(ndict, 'r', encoding='utf-8')
fh2 = open(compcat, 'r', encoding='utf-8')

# 存取要查找的新聞標題
stringlist = []
for string in fh0:
    string = string.split(' ')
    string = ''.join(string)
    stringlist.append(string)

# 把關鍵字權重變成字典
newsdict = dict()
for d in fh1:
    d = d.strip('\n')
    d = d.split(' ')
    newsdict[d[0]] = int(d[1])
newsdict = sorted(newsdict.items(), reverse=True, key=lambda x: len(x[0]))

# 把公司和對應股票類別變成字典
stocktype = dict()
for s in fh2:
    s = s.strip('\n')
    s = s.split(' ')
    if s[1] not in stocktype:
        stocktype[s[1]] = [s[0]]
    else:
        stocktype[s[1]].append(s[0])

# 計算類股公司分數
score = dict()
for t in stocktype[target]:
    for s in stringlist:
        # 找公司名稱
        comp = s.find(t)
        if comp == -1:
            continue
        else:
            # 如果公司名稱存在開始算關鍵字權重
            for d in newsdict:
                kindex = s.find(d[0])
                # 如果關鍵字不存在在標題裡就換下一個
                if kindex == -1:
                    continue
                else:
                    # 計算各家公司分數
                    if t not in score:
                        score[t] = d[1]
                    else:
                        score[t] += d[1]

# 整理公司分數排名
sorted_comp = sorted(score.items(), key=lambda x: (x[1], x[0]), reverse=True)
sorted_comp = sorted_comp[:len(rquant)]

# 計算最終購買的迴圈
finalbuy = dict()
for i in sorted_comp:
    finalbuy[i[0]] = 0
while targetq >= 0:
    for c in range(len(sorted_comp)):
        # 如果應買數量比分配數量多
        if targetq >= rquant[c]:
            # 直接買分配數量
            finalbuy[sorted_comp[c][0]] += rquant[c]
        else:
            # 不然就把剩下應買數量買完
            finalbuy[sorted_comp[c][0]] += targetq
        targetq -= rquant[c]
        if targetq < 0:
            break

if target not in stocktype:
    print('NO_MATCH')
else:
    for i in sorted_comp:
        if finalbuy[i[0]] == 0:
            pass
        else:
            txt = '{}購買{}張'.format(i[0], finalbuy[i[0]])
            print(txt)
