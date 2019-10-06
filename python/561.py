# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 0006 9:09
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 561.py
# @Software: PyCharm

class Solution:
    def arrayPairSum(self, nums: list) -> int:
        nums=sorted(nums)
        n=len(nums)
        sum=0
        for i in range(0,n,2):
            sum+=nums[i]
        return sum

if __name__=="__main__":
    nums=[1,4,3,2]
    so=Solution()
    a=so.arrayPairSum(nums)
    print(a)
