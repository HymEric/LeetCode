# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 0023 16:05
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 556.py
# @Software: PyCharm
import random
class Solution:
    def matrixReshape(self, nums:list, r: int, c: int):
        # record row and col
        ori_r=len(nums)
        ori_c=len(nums[0])
        ori_num=ori_c*ori_r
        # print(ori_num)
        if r*c !=ori_num:
            return nums
        flatten_nums=[]
        # flatten nums
        for i in range(ori_r):
            for j in range(ori_c):
                flatten_nums.append(nums[i][j])
        print(flatten_nums)
        new_num=[[0]*c for row in range(r)]
        # new_num = [[0] * c]*r
        # new_num=[[]]
        ind=0
        for i in range(r):
            for j in range(c):
                new_num[i][j]=flatten_nums[ind]
                ind+=1

        return new_num

    def matrixReshape2(self, nums:list, r: int, c: int):
        # record row and col
        ori_r=len(nums)
        ori_c=len(nums[0])
        ori_num=ori_c*ori_r
        # print(ori_num)
        if r*c !=ori_num:
            return nums
        a=[]
        b=[]
        cnt_c=0
        for i in range(ori_r):
            for j in range(ori_c):
                print(nums[i][j])
                b.append(nums[i][j])
                print(b)
                cnt_c+=1
                if cnt_c == c:
                    a.append(b)
                    b = []
                    cnt_c=0

        def matrixReshape3(self, nums: list, r: int, c: int):
            # record row and col
            ori_r = len(nums)
            ori_c = len(nums[0])
            ori_num = ori_c * ori_r
            # print(ori_num)
            if r * c != ori_num:
                return nums
            a = []
            b = []
            cnt_c = 0
            for i in range(ori_r):
                for j in range(ori_c):
                    print(nums[i][j])
                    b.append(nums[i][j])
                    print(b)
                    cnt_c += 1
                    if cnt_c == c:
                        a.append(b)
                        b = []
                        cnt_c = 0
        return a

if __name__=="__main__":
    nums =[[1, 2],[3, 4]]
    so=Solution()
    result=so.matrixReshape(nums,4,1)
    print(result)
