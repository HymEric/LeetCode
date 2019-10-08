# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 19:58
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 189.py
# @Software: PyCharm

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i=0
        k=k%len(nums)
        for i in range(len(nums)-k):
            nums.append(nums[0])
            nums.pop(0)
            # i+=1
        # print(nums)
        return nums

    def rotate2(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        for _ in range(k):
            nums.insert(0,nums.pop())
        return nums

    def rotate3(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
        return nums

if __name__=="__main__":
    nums=[1,2,3]
    so=Solution()
    a=so.rotate(nums,4)
    print(a)
