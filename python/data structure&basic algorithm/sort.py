# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 0011 16:43
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : sort.py
# @Software: PyCharm
"""
各种排序算法合集
"""
class Solution:
    def MergeSort(self,nums:list): # 归并排序
        def sort(nums:list,left:int,right:int):
            # print(left,right)
            if left==right:
                return
            mid=left+((right-left)>>1)
            sort(nums,left,mid) # sort left part
            sort(nums,mid+1,right) # sort right part
            merge(nums,left,mid,right) # merge
            # print(nums)
        def merge(nums:list,left,mid,right):
            # print(left,right)
            res=[] # create temperate list
            p1=left # left start of left part
            p2=mid+1 # right start of right part
            while p1<=mid and p2<=right:
                if nums[p1]<=nums[p2]:
                    res.append(nums[p1])
                    p1+=1
                else:
                    res.append(nums[p2])
                    p2+=1
                # res.append(nums[p1] if nums[p1]<=nums[p2] else nums[p2])
            while(p1<=mid):
                res.append(nums[p1])
                p1+=1
            while(p2<=right):
                res.append(nums[p2])
                p2+=1
            # print(res)
            for i in range(len(res)):
                # print(left+i)
                nums[left+i]=res[i]
            # print(nums)
            del res
        sort(nums,0,len(nums)-1)


if __name__=="__main__":
    a=[23,12,22,11,4,2]
    s=Solution()
    s.MergeSort(a)
    print(a)