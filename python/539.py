# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 18:15
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 539.py
# @Software: PyCharm

class Solution:
    def findMinDifference(self, timePoints:list) -> int:
        timeMin=[]
        for time_ in timePoints:
            min_ = int(time_[0:2]) * 60 + int(time_[3:])
            timeMin.append(min_)
        if len(timePoints)==2:
            temp=min(abs(timeMin[0]-timeMin[1]),1440-abs(timeMin[0]-timeMin[1]))
            return temp
        cumsub=[]
        # print(timeMin)
        timeMin=sorted(timeMin)
        # print(timeMin)
        for i in range(len(timeMin)-1):
            cumsub.append(timeMin[i+1]-timeMin[i])
        cumsub.append(min(timeMin[-1]-timeMin[0],1440-timeMin[-1]+timeMin[0]))
        cumsub=sorted(cumsub)

        return cumsub[0]

    def findMinDifference2(self, timePoints: list) -> int:
        timeMin=[]
        for time_ in timePoints:
            temp=int(time_[0:2]) * 60 + int(time_[3:])
            if temp in timeMin:
                return 0
            timeMin.append(temp)
        timeMin.sort()
        timeMin=timeMin+[timeMin[0]+1440] # for first element subtract last
        temp=1440
        for i in range(1,len(timeMin)):
            temp=min(temp,timeMin[i]-timeMin[i-1])
        return temp

if __name__=="__main__":
    word= ["11：40","13:00"]
    so=Solution()
    a=so.findMinDifference(word)
    print(a)
