# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 15:51
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 551.py
# @Software: PyCharm

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s==None:
            return None
        if s.count('A')>1:
            return False
        if 'LLL' in s:
            return False
        return True

    def checkRecord2(self, s: str) -> bool:
        return not (len(s.split('A')) > 2 or "LLL" in s)

    def checkRecord3(self, s: str) -> bool:
        return s.count('A')<2 and s.count('LLL')<1

if __name__=="__main__":
    s="PPALLL"
    so=Solution()
    a=so.checkRecord3(s)
    print(a)
