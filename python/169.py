# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 19:31
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 169.py
# @Software: PyCharm
import collections
class Solution:
    def majorityElement(self, nums: list) -> int:
        nums_dict={}
        for i in range(len(nums)):
            if nums_dict.get(nums[i]):
                nums_dict[nums[i]]+=1
            else:
                nums_dict[nums[i]]=1

        # nums_dict=sorted(nums_dict.items(),key=lambda x: x[1],reverse=True)
        # print(nums_dict)
        # return nums_dict[0][0]
        return max(nums_dict.items(),key=lambda x:x[1])[0]
    def majorityElement2(self, nums: list) -> int:
        counts=collections.Counter(nums)
        print(counts)
        return max(counts.keys(),key=counts.get)
if __name__=="__main__":
    nums=[2,2,3]
    so=Solution()
    a=so.majorityElement(nums)
    print(a)
