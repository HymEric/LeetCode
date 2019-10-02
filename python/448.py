# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 0002 20:41
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 448.py
# @Software: PyCharm

class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        """
        利用数组大小在1-n之间和数组大小为n的关系求解，我们相处一个标记是这样的，
        当前数组元素1<=nums[i]<=n，则0<=nums[i]-1<=n-1即是数组index下标的区间，
        我们让所有nums[nums[i]]=-nums[i]，这样因为原始的数组都是正整数，所以数组
        中的整数的下标+1代表了没有出线在原始数组中的数
        :param nums:
        :return:
        """
        if nums==None:
            return None
        for i in range(len(nums)):
            ind=abs(nums[i])-1 # avoiding the pre-set influence and out of range
            nums[ind]=-abs(nums[ind])
        print(nums)
        return [i+1 for i in range(len(nums)) if nums[i]>0]

    # over time 判断的速度比查找的速度快的多
    def findDisappearedNumbers2(self, nums: list) -> list:
        if nums == None:
            return None
        n = len(nums)
        new_nums = list(set(nums))
        temp = []
        for i in range(1, n + 1, 1):
            if i not in new_nums:
                temp.append(i)
        return temp
if __name__=="__main__":
    nums= [4,3,2,7,8,2,3,1]
    so=Solution()
    a=so.findDisappearedNumbers(nums)
    print(a)
