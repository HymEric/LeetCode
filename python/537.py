# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 16:03
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 537.py
# @Software: PyCharm

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        plus_ind1=a.find('+')
        plus_ind2 = b.find('+')
        a1=int(a[0:plus_ind1])
        b1=int(a[plus_ind1+1:-1])
        a2=int(b[0:plus_ind2])
        b2=int(b[plus_ind2+1:-1])
        return str(int(a1*a2-b1*b2))+"+"+str(int(a1*b2+b1*a2))+"i"

if __name__=="__main__":
    a="78+-76i"
    b="-86+72i"
    so=Solution()
    a=so.complexNumberMultiply(a,b)
    print(a)
