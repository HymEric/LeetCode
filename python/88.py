# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 19:12
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 88.py
# @Software: PyCharm

class Solution:
    def merge(self, nums1:list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind_1=m-1
        ind_2=n-1
        i=len(nums1)-1
        while(ind_1>=0 and ind_2>=0):
            if nums1[ind_1]>=nums2[ind_2]:
                nums1[i]=nums1[ind_1]
                ind_1-=1
            else:
                nums1[i]=nums2[ind_2]
                ind_2-=1
            i-=1
        while(ind_1>=0):
            nums1[i]=nums1[ind_1]
            ind_1-=1
            i-=1
        while (ind_2 >= 0):
            nums1[i] = nums2[ind_2]
            ind_2 -= 1
            i -= 1
        return nums1

if __name__=="__main__":
    nums1 = [1, 3,7, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    so=Solution()
    a=so.merge(nums1,m,nums2,n)
    print(a)
