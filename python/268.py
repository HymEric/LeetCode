# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 0005 14:47
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 268.py
# @Software: PyCharm

class Solution:
    def missingNumber(self, nums: list) -> int:
        n=len(nums)
        nums_dict={}
        for i in range(n):
            nums_dict[nums[i]]=1
        for j in range(n+1):
            if nums_dict.get(j)==None:
                return j
        return None

    def missingNumber2(self, nums: list) -> int:
        s1,s2=set(range(len(nums))),set(nums)
        return len(nums) if s1==s2 else list(s1-s2)[0]

    def missingNumber3(self, nums: list) -> int:
        missing=len(nums)
        for i in range(len(nums)):
            missing=missing^nums[i]^i
        return missing

if __name__=="__main__":
    nums=[9,6,4,2,3,5,7,0,1]
    so=Solution()
    a=so.missingNumber3(nums)
    print(a)
