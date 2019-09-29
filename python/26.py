# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 0029 22:18
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 26.py
# @Software: PyCharm

class Solution:
    # over time
    def removeDuplicates(self, nums: list) -> int:
        ori_len=len(nums)
        k=0
        for i in range(len(nums)):
            # print(nums)
            i=i-k
            number=nums.count(nums[i])
            if number >1:
                nums.pop(i)
                ori_len-=1
                k+=1

        return ori_len
    # right
    def removeDuplicates2(self, nums: list) -> int:
        if nums==None or len(nums) <0:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k

if __name__=="__main__":
    nums= [1,1,2]
    so=Solution()
    a=so.removeDuplicates2(nums)
    print(a)
