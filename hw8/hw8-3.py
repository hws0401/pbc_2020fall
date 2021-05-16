# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:25:28 2021

@author: Ruby
"""

from datetime import datetime
# 第一行日期
datestr = input()
datestr = datestr.replace('/',' ')
today_date = datetime.strptime(datestr, '%Y %m %d').date()
# 第二行任務和狗名字
task = input().split(',')

class Dog:
    def __init__(self, name, height, weight, adopted_date):
        self.name = name
        self.height = height 
        self.weight = weight 
        self.adopted_date = adopted_date
        self.dust = 0
        self.walk_count = 0
        self.longest_duration = 0
        self.last_walk_date = adopted_date
        self.is_small_dog = self.check_if_small_dog()
        self.walk_frequency = 0

    def check_if_small_dog(self):  # 判斷是否為小型犬，回傳 boolean 值
        if self.height > 60:
            return False
        elif self.weight > 30:
            return False
        else:
            return True

    def walk(self, walk_date): 
        if self.is_small_dog:  # 依據小型犬的灰塵累積效率更新累積灰塵量
            self.dust += 3
        else:  # 依據大型犬的灰塵累積效率更新累積灰塵量
            self.dust += 2
		# 更新散步次數、最大散步間隔時間、最近散步日期
        self.walk_count += 1
        duration = (walk_date - self.last_walk_date).days
        if duration > self.longest_duration:
            self.longest_duration = duration
        self.last_walk_date = walk_date
        return self.dust, self.walk_count, self.longest_duration, self.last_walk_date

    def bathe(self):  # 更新累積灰塵量
        self.dust = 0
        return self.dust
    
    def calculate_frequency(self, today_date):  # 計算散步頻率
        total_days = (today_date - self.adopted_date).days
        self.walk_frequency = self.walk_count / total_days
        return self.walk_frequency


# 紀錄輸入迴圈
doglist = []
while True:
    record = input().split('|')
    if record[0] == 'A':
        thedog = record[1]
        adatestr = record[4].replace('/',' ')
        adateob = datetime.strptime(adatestr, '%Y %m %d').date()
        thedog = Dog(record[1], int(record[2]), int(record[3]), adateob)
        doglist.append(thedog)
    elif record[0] == 'B':
        for thedog in doglist:
            if thedog.name == record[1]:
                thedog.bathe()
    elif record[0] == 'W':
        wdatestr = record[2].replace('/',' ')
        wdateob = datetime.strptime(wdatestr, '%Y %m %d').date()
        for thedog in doglist:
            if thedog.name == record[1]:
                thedog.walk(wdateob)
    elif record[0] == 'L':
        for thedog in doglist:
            if thedog.name == record[1]:
                doglist.remove(thedog)
    elif 'Done' in record:
        break

# 找到該執行的任務
minwalk_list = []
maxduration_lst = []
maxdust_list = []
flag = []
targetdog = ''
# 找名字一樣的狗
if task[0] == 'TaskA':
    for dogs in doglist:
        if dogs.name == task[1]:
            targetdog == dogs
# 找散步頻率最低的狗
if task[0] == 'TaskB':
    minfre = 2
    for dogs in doglist:
        # 算狗的散步頻率
        dogs.calculate_frequency(today_date)
        # 找出散步頻率最低的狗
        if dogs.walk_frequency < minfre:
            minfre = dogs.walk_frequency
            flag = []
            flag.append(dogs)
        elif dogs.walk_frequency == minfre:
            flag.append(dogs)
    # 如果找到多於一隻狗
    # 剔除小型狗
    if len(flag) > 1:
        if all(dogs.is_small_dog == True for dogs in flag):
            pass
        else:
            for dogs in flag:
                if dogs.is_small_dog:
                    flag.remove(dogs)
        # 剔除體重不夠重的狗
        if len(flag) > 1:
            flag.sort(key=lambda x:x.weight, reverse=True)
            heaviest = flag[0].weight
            for dogs in flag:
                if dogs.weight < heaviest:
                    flag.remove(dogs)
            # 選身高高的狗
            if len(flag) > 1:
                flag.sort(key=lambda x:x.height, reverse=True)
                tallest = flag[0].height
                for dogs in flag:
                    if dogs.height < tallest:
                        flag.remove(dogs)
                # 名字開頭字母最前面
                if len(flag) > 1:
                    flag.sort(key=lambda x:x.name)
                    targetdog = flag[0]
            else:
                targetdog = flag[0]
        else:
            targetdog = flag[0]
    else:
        targetdog = flag[0]
# 找散步時間間隔最長的狗
if task[0] == 'TaskC':
    doglist.sort(key=lambda x: x.longest_duration, reverse=True)
    longest = doglist[0].longest_duration
    flag = []
    for dogs in doglist:
        if dogs.longest_duration > longest:
            flag = []
            flag.append(dogs)
        elif dogs.longest_duration == longest:
            flag.append(dogs)
    # 如果找到多於一隻狗
    # 剔除小型狗
    if len(flag) > 1:
        if all(dogs.is_small_dog == True for dogs in flag):
            pass
        else:
            for dogs in flag:
                if dogs.is_small_dog:
                    flag.remove(dogs)
        # 剔除體重不夠重的狗
        if len(flag) > 1:
            flag.sort(key=lambda x:x.weight, reverse=True)
            heaviest = flag[0].weight
            for dogs in flag:
                if dogs.weight < heaviest:
                    flag.remove(dogs)
            # 選身高高的狗
            if len(flag) > 1:
                flag.sort(key=lambda x:x.height, reverse=True)
                tallest = flag[0].height
                for dogs in flag:
                    if dogs.height < tallest:
                        flag.remove(dogs)
                # 名字開頭字母最前面
                if len(flag) > 1:
                    flag.sort(key=lambda x:x.name)
                    targetdog = flag[0]
            else:
                targetdog = flag[0]
        else:
            targetdog = flag[0]
    else:
        targetdog = flag[0]
# 找灰塵累積最多的狗
if task[0] == 'TaskD':
    doglist.sort(key=lambda x: x.dust, reverse=True)
    dustiest = doglist[0].dust
    flag = []
    for dogs in doglist:
        if dogs.dust > dustiest:
            flag = []
            flag.append(dogs)
        elif dogs.dust == dustiest:
            flag.append(dogs)
    # 如果找到多於一隻狗
    # 剔除小型狗
    if len(flag) > 1:
        if all(dogs.is_small_dog == True for dogs in flag):
            pass
        else:
            for dogs in flag:
                if dogs.is_small_dog:
                    flag.remove(dogs)
        # 剔除體重不夠重的狗
        if len(flag) > 1:
            flag.sort(key=lambda x:x.weight, reverse=True)
            heaviest = flag[0].weight
            for dogs in flag:
                if dogs.weight < heaviest:
                    flag.remove(dogs)
            # 選身高高的狗
            if len(flag) > 1:
                flag.sort(key=lambda x:x.height, reverse=True)
                tallest = flag[0].height
                for dogs in flag:
                    if dogs.height < tallest:
                        flag.remove(dogs)
                # 名字開頭字母最前面
                if len(flag) > 1:
                    flag.sort(key=lambda x:x.name)
                    targetdog = flag[0]
            else:
                targetdog = flag[0]
        else:
            targetdog = flag[0]
    else:
        targetdog = flag[0]

print('{0},{1},{2},{3}'.format(targetdog.name, targetdog.height, targetdog.weight, targetdog.dust))