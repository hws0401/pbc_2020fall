# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:52:45 2020

@author: Ruby
"""
# -*-coding: utf8-*-
keyword = input()

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

# 找出關鍵字位置
start = 0
end = len(stringlist)
xlist = []
for s in stringlist:
    index = stringlist.find(keyword, start, end)
    if index == -1:
        break
    else:
        xlist.append(index)
        start += 1

# 整理關鍵字LIST
if not xlist:
    print('NO_MATCH')
else:
    # 刪去重複INDEX
    newlist = []
    for i in xlist:
        if i not in newlist:
            newlist.append(i)
    # 避免LOOP到倒數INDEX
    for n in newlist:
        front = n - 7
        back = n + 7
        if front < 0:
            keystring = stringlist[0:n] + '**'\
                        + keyword + '**'\
                        + stringlist[n + len(keyword):n + len(keyword) + 7]
            print(keystring)
        else:
            keystring = stringlist[n-7:n] + '**'\
                        + keyword + '**'\
                        + stringlist[n + len(keyword):n + len(keyword)+7]
            print(keystring)
