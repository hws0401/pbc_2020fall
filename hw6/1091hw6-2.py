# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:06:16 2020

@author: Ruby
"""

# -*-coding: utf8-*-
space = int(input())
keyword1 = input()
keyword2 = input()

# 存取要查找的句子
stringlist = []
while True:
    string = input()
    if string == 'INPUT_END':
        break
    else:
        string = string.strip()
        stringlist.append(string)
stringlist = ' '.join(stringlist)

# 找第一個關鍵字
start = 0
end = len(stringlist)
keylist1 = []
for s in stringlist:
    index = stringlist.find(keyword1, start, end)
    if index == -1:
        break
    else:
        keylist1.append(index)
        start += 1

# 找第二個關鍵字
start = 0
end = len(stringlist)
keylist2 = []
for s in stringlist:
    index = stringlist.find(keyword2, start, end)
    if index == -1:
        break
    else:
        keylist2.append(index)
        start += 1
# 如果沒有找到任何關鍵字
if not keylist1 and (not keylist2):
    print('NO_MATCH')
# 如果有找到關鍵字
else:
    # 刪去重複INDEX
    newlist1 = []
    for i in keylist1:
        if i not in newlist1:
            newlist1.append(i)
    # 關鍵字二間隔跟順序確認
    newlist2 = []
    for i in keylist2:
        if i not in newlist2:
            newlist2.append(i)
    if not newlist1 or (not newlist2):
        print('NO_MATCH')
    else:
        # 關鍵字配對
        keypair = []
        for n in newlist1:
            for nn in newlist2:
                pairlist = []
                if nn-n <= len(keyword1)+space and n-nn < 0:
                    pairlist.append(n)
                    pairlist.append(nn)
                    keypair.append(pairlist)
        if not keypair:
            print('NO_MATCH')
        else:
            # 印出
            for k in keypair:
                k1 = k[0]
                k2 = k[1]
                front = k1 - 7
                if front < 0:
                    keystring = stringlist[0:k1]\
                                + '**' + keyword1 + '**' \
                                + stringlist[k1+len(keyword1):k2] \
                                + '**' + keyword2 + '**' \
                                + stringlist[k1+len(keyword2):k2+len(keyword2)+7]
                    print(keystring.strip())
                else:
                    keystring = stringlist[front:k1] \
                                + '**' + keyword1 + '**' \
                                + stringlist[k1+len(keyword1):k2] \
                                +'**' + keyword2 + '**' \
                                + stringlist[k2+len(keyword2):k2+len(keyword2)+7]
                    print(keystring.strip())
