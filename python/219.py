# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 0026 20:47
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 219.py
# @Software: PyCharm

class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        if len(nums)<0 or nums==None:
            return False
        nums_dict={}
        for i in range(len(nums)):
            # print(nums_dict.keys())
            if nums[i] in nums_dict.keys():
                # print(nums[i])
                if i-nums_dict[nums[i]]<=k:
                    return True
                else:
                    nums_dict.update({nums[i]:i})
            nums_dict[nums[i]]=i
        return False

if __name__=="__main__":
    nums=[1,2,3,1,2,3]
    so=Solution()
    a=so.containsNearbyDuplicate(nums,2)
    print(a)
