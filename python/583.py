# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 0001 20:16
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 583.py
# @Software: PyCharm

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1,1):
            for j in range(1,n+1,1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # the final element in dp is the longest number of LCS
        return m+n-2*dp[m][n]

if __name__=="__main__":
    w1=''
    w2='a'
    so=Solution()
    a=so.minDistance(w1,w2)
    print(a)