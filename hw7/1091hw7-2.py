# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:53:02 2020

@author: Ruby
"""
# 讀入檔案
inputm = input()
inputg = input()
mvid = input()
fh0 = open(inputm, 'r', encoding='ISO-8859-1')
fh1 = open(inputg, 'r', encoding='ISO-8859-1')

# 整理電影資料切割成list
movie = []
for aline in fh0:
    aline = aline.strip('\n')
    minfo = aline.split('|')
    movie.append(minfo)

# 整理類別資料切割成list
genre = []
for g in fh1:
    g = g.strip('\n')
    gen = g.split('|')
    genre.append(gen)

movgen = dict()
for m in movie:
    # 建立字典，寫入ID和對應片名
    movgen[m[0]] = [m[1]]
    for mm in range(5, len(m)):
        # 不是這個類別就跳過
        if m[mm] == '0':
            continue
        else:
            mmi = mm - 5
            # 在對應的電影加入所屬類別
            for gg in genre:
                if mmi == genre.index(gg):
                    movgen[m[0]].append(gg[0])

# 印出格式排版
if mvid in movgen:
    pstring = movgen[mvid][0] + ': '
    for i in movgen[mvid][1:]:
        if i == movgen[mvid][-1]:
            pstring += i
        else:
            pstring += i + ', '
    print(pstring)
else:
    # 如果該ID電影不存在
    print('No movie found.')
