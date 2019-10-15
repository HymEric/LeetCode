# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 16:56
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 151.py
# @Software: PyCharm

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        temp=s.split(' ')
        rev=''
        for i in range(len(temp)-1,-1,-1):
            if temp[i]!='':
                rev+=temp[i]+' '
        return rev.strip()
    def reverseWords2(self, s: str) -> str:
        return " ".join(s.split()[::-1])

if __name__=="__main__":
    word="a good   example"
    so=Solution()
    a=so.reverseWords2(word)
    print(a)
