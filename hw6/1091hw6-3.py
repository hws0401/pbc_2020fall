# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:06:27 2020

@author: Ruby
"""
# -*-coding: utf8-*-
company = input().split(',')
keygroup = input().split(',')

# 存取要查找的新聞標題
stringlist = []
while True:
    string = input()
    if string == 'INPUT_END':
        break
    else:
        string = string.split(' ')
        string = ''.join(string)
        stringlist.append(string)

# 將關鍵字照長度排序
keygroup.sort(key=len, reverse=True)

# 替換字元用
temp = []
for s in stringlist:
    temp.append(s)

# 找各句關鍵字
allkey = []
for t in temp:
    keylist = []
    for k in keygroup:
        kindex = t.find(k)
        keylist.append(kindex)
        t = t.replace(k, ('\u265E')*len(k))
    allkey.append(keylist)

# 開始切
addup = 0
for s in range(len(stringlist)):
    prevkey = 99999
    for k in allkey[s]:
        if k == -1:
            pass
        else:
            print(prevkey, k)
            if prevkey < k:
                addup += 2
            else: 
                pass
            print(addup)
            stringlist[s] = stringlist[s][0:k+addup] + '/' \
                        + keygroup[allkey[s].index(k)] + '/' \
                        + stringlist[s][k+addup+len(keygroup[allkey[s].index(k)]):99999]
            prevkey = k
            print(stringlist[s])

# 去重複符號
for s in stringlist:
    s = s.replace('//', '/')

# 找標題對應公司
clist = []
for s in stringlist:
    ctrue = []
    prevc = -1
    for c in company:
        cindex = s.find(c)
        if cindex == -1:
            pass
        else:
            if cindex < prevc:
                ctrue.insert(previndex-1, company.index(c))
            else:
                ctrue.append(company.index(c))
            previndex = ctrue.index(company.index(c))
            prevc = cindex
    clist.append(ctrue)

# 有標題對公司才印
for c in range(len(clist)):
    if not clist[c]:
        stringlist[c] = 'NO_MATCH'
    else:
        companystring = ''
        count = len(clist[c])
        for cc in clist[c]:
            if count == 1:
                companystring += company[cc]
            else:
                companystring += company[cc] + ','
                count -= 1
        stringlist[c] = companystring + ';' + stringlist[c]

for s in stringlist:
    print(s)
