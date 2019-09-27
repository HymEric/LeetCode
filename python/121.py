# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 0027 18:40
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 121.py
# @Software: PyCharm


class Solution:
    def maxProfit(self, prices: list) -> int:
        if prices==None or len(prices)<=1:
            return 0
        for i in range(len(prices)):
            if i ==0:
                low=prices[i]
                high=prices[i]
                low_id=i
                high_id=i
            else:
                if prices[i]<=low and max(prices[i:])-prices[i]>high-low:
                    low=prices[i]
                    low_id=i
                    high=-1
                    high_id=-1
                elif high==-1 or prices[i]>high:
                    high=prices[i]
                    high_id=i
        # print(high)
        # print(low)
        if high_id>low_id:
            return high-low
        return 0

    def maxProfit2(self, prices: list) -> int:
        # record min value and the max value - min value as max_profit
        min_p=float('inf')
        max_profit=0
        for i in range(len(prices)):
            min_p=min(min_p,prices[i])
            max_profit=max(max_profit,prices[i]-min_p)
        return max_profit


if __name__=="__main__":
    nums=[2,1,4]
    so=Solution()
    a=so.maxProfit2(nums)
    print(a)
