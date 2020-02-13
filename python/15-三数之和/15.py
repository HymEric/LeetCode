# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 0012 18:43
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 15.py
# @Software: PyCharm
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def threeSum(self, nums: list) -> list:
        if nums==None or len(nums)<3:
            return []
        nums.sort()
        print(nums)
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0: # succeed, move to next location
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    while l<r and nums[r+1]==nums[r]:
                        r-=1

                elif nums[i]+nums[l]+nums[r]>0: # sum too large, r should move to left
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0: # sum too small, l should move to right
                    l+=1
        return res

if __name__=="__main__":
    s1 =[-2,0,1,1,2]
    so=Solution()
    a=so.threeSum(s1)
    print(a)