# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 0028 18:41
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 66.py
# @Software: PyCharm

class Solution:
    def plusOne(self, digits: list) ->list:
        k=0
        for i in range(-1,-len(digits)-1,-1):
            digits[i]=digits[i]+k
            k=0
            if i==-1:
                digits[i] = digits[i] + 1
            if digits[i]>9:
                k=digits[i]//10
                digits[i]=digits[i]%10
        if k !=0 :
            digits.insert(0,k)
        return digits


if __name__=="__main__":
    nums= [4,3,2,1]
    so=Solution()
    a=so.plusOne(nums)
    print(a)
