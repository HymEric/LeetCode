# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 0001 15:03
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 27.py
# @Software: PyCharm
"""
note: change the element value in original list
"""
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        k=0
        cnt=nums.count(val)
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        print(nums)
        return len(nums)-cnt

if __name__=="__main__":
    nums= [0,1,2,2,3,0,4,2]
    so=Solution()
    a=so.removeElement(nums,2)
    print(a)
