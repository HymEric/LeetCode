# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 0005 9:15
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 217.py.py
# @Software: PyCharm

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        nums_dict={}
        for i in range(len(nums)):
            if nums_dict.get(nums[i])!=None:
                return True
            nums_dict[nums[i]]=1
        return False

    def containsDuplicate2(self, nums: list) -> bool:
        return len(nums) != len(set(nums))

if __name__=="__main__":
    nums=[1,2]
    so=Solution()
    a=so.containsDuplicate(nums)
    print(a)
