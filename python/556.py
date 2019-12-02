# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 0002 8:37
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 556.py
# @Software: PyCharm
"""
556. Next Greater Element III
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n,tail=list(str(n)),[]
        for i in range(len(n)-1,-1,-1):
            for j in tail:
                if n[j]>n[i]:
                    n[i],n[j]=n[j],n[i]
                    m=int(''.join(n[:i+1]+sorted(n[i+1:])))
                    return -1 if m>2**31-1 else m
            tail.append(i)
        return -1

if __name__=="__main__":
    n=231
    so=Solution()
    a=so.nextGreaterElement(n)
    print(a)