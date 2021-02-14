# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:05:24 2020

@author: Ruby
"""
import operator

# 讀入檔案和關鍵字
fn0 = input()
keyword = input()
fh0 = open(fn0, 'r', encoding='utf-8')

# 去頭尾空白裝進list
senlist = []
for aline in fh0:
    twosen = aline.split('\t')
    for s in twosen:
        s = s.strip()
        s = s.strip('\n')
        senlist.append(s)

# locate關鍵字
keyfront = dict()
keyrear = dict()
for s in senlist:
    start = 0
    end = len(s)
    rawkey = []
    # 逐字iterate直到句內找不到關鍵字
    for ss in range(len(s)):
        kindex = s.find(keyword, start, end)
        if kindex == -1:
            break
        else:
            start += 1
            rawkey.append(kindex)
    newlist = []
    # 刪掉重複index
    for k in rawkey:
        if k not in newlist:
            newlist.append(k)
    # 句內沒有關鍵字就跳下一句
    if not newlist:
        continue
    else:
        for n in newlist:
            frontk = n-1
            reark = n+len(keyword)
            # 先取熱門前一字
            if frontk < 0:  # 避免取到倒數幾個字
                pass
            else:
                # 在字典內就加一，不在則創造新key
                if s[frontk] in keyfront:
                    keyfront[s[frontk]] += 1
                else:
                    keyfront[s[frontk]] = 1
            # 再取熱門後一字
            if reark >= len(s):  # 避免list index out of range
                pass
            else:
                # 在字典內就加一，不在則創造新key
                if s[reark] in keyrear:
                    keyrear[s[reark]] += 1
                else:
                    keyrear[s[reark]] = 1

# 照次數整理順序
sorted_f = sorted(keyfront.items(), key=operator.itemgetter(1, 0), reverse=True)
sorted_r = sorted(keyrear.items(), key=operator.itemgetter(1, 0), reverse=True)

print('熱門前一個字:')
for k in sorted_f[:10]:
    print(k[0] + '---' + keyword)
print('熱門下一個字:')
for k in sorted_r[:10]:
    print(keyword + '---' + k[0])
