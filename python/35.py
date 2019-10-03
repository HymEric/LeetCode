# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 0003 21:11
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 35.py
# @Software: PyCharm

class Solution:
    # simple
    def searchInsert(self, nums: list, target: int) -> int:
        try:
            ind=nums.index(target)
        except:
            for i in range(len(nums)):
                if nums[i]>target:
                    nums.insert(i,target)
                    ind=i
                    return ind
            return len(nums)
        else:
            return ind
    # binary divide
    def searchInsert2(self, nums: list, target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__=="__main__":
    nums= [1,3,5,6]
    so=Solution()
    a=so.searchInsert2(nums,0)
    print(a)
