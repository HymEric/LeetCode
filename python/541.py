# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 0019 19:37
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 541.py
# @Software: PyCharm
"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""


class Solution:
    # def reverseStr(self, s: str, k: int) -> str:
    #     if s is None:
    #         return None
    #     res = ""
    #     length=len(s)
    #     if length<k:
    #         for p in range(length-1,-1,-1):
    #             res=res+s[p]
    #         return res
    #     k_2=2*k # for every 2k
    #     i=0
    #     while(i<length):
    #         # print(i)
    #         if i%k_2==0:
    #             for t in range(i+k-1,i-1,-1):
    #                 res=res+s[t]
    #                 # print(res)
    #             i=i+k-1
    #             # print(i)
    #         else:
    #             res=res+s[i]
    #         i+=1
    #
    #     return res

    def reverseStr2(self, s: str, k: int) -> str:
        a=list(s)
        for i in range(0,len(a),2*k):
            a[i:i+k]=reversed(a[i:i+k])
        return "".join(a)

if __name__=="__main__":
    s="abcde"
    k=2
    so=Solution()
    a=so.reverseStr2(s,k)
    print(a)