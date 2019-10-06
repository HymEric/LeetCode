# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 0006 9:41
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 283.py
# @Software: PyCharm

class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=i+1
        while(j<len(nums)):
            # print(i,j)
            if nums[i]==0 and nums[j]!=0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]==0:
                j+=1
            else:
                j+=1
                i+=1
        return nums

    def moveZeroes2(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[k]
                nums[k]=temp
                k+=1
        return nums



if __name__=="__main__":
    nums=[0,0,0,1]
    so=Solution()
    a=so.moveZeroes(nums)
    print(a)
