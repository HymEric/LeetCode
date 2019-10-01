# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 0001 14:00
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 532.py
# @Software: PyCharm
"""
use Set to avoiding repeated number automatically
return len(Set)
"""

class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        if k <0:
            return 0;
        raw,diff=set(),set()
        for num in nums:
            if num-k in raw:
                diff.add(num-k)
            if num + k in raw:
                diff.add(num)
            raw.add(num)
        print(raw)
        print(diff)
        return len(diff)

    def findPairs2(self, nums: list, k: int) -> int:
        if k <0:
            return 0
        # first for k==0
        if k ==0:
            num_dict={}
            rep=set() # for saving num and avoid repeating
            for num in nums:
                if num in num_dict.keys():
                    rep.add(num)
                else:
                    num_dict[num]=0
            return len(rep)
        # second there is not duplicated number
        cnt = 0
        nums_new=list(set(nums))
        for num in nums_new:
            if num-k in nums_new:
                cnt+=1
            # if  num+k in nums_new:
            #     cnt+=1
        return cnt

if __name__=="__main__":
    nums=[1,1,1,1,1]
    so=Solution()
    a=so.findPairs2(nums,0)
    print(a)
