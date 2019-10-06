# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 0006 15:31
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 167.py
# @Software: PyCharm

class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        low,high=-1,-1
        for i in range(len(numbers)):
            try:
                j=numbers.index(target-numbers[i],i+1)
            except:
                # print(i)
                if i == len(numbers)-1:
                    return None
            else:
                low=i
                high=j
                break
        return [low+1,high+1]
    def twoSum2(self, numbers: list, target: int) -> list:
        low,high=-1,-1
        nums_dict={}
        for i in range(len(numbers)):
            nums_dict[numbers[i]]=i
        for i in range(len(numbers)):
            j=nums_dict.get(target-numbers[i])
            if j!=None and i!=j:
                low=i
                high=j
                break
        return [low+1,high+1]
if __name__=="__main__":
    nums=[0,0,11,15]
    so=Solution()
    a=so.twoSum2(nums,11)
    print(a)
