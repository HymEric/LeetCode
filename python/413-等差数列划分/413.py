# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 0031 17:38
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 413.py
# @Software: PyCharm
"""
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

 

示例:

A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def numberOfArithmeticSlices(self, A: list) -> int: # violence
        if A==None or len(A)<=2:
            return 0
        count=0
        for i in range(0,len(A)-2,1):
            d=A[i+1]-A[i]
            for j in range(i+2,len(A),1):
                t=i+1
                while(t<=j):
                    if A[t]-A[t-1]!=d:
                        break
                    t+=1
                if t>j:
                    count+=1
        return count
    def numberOfArithmeticSlices2(self, A: list) -> int: # optimized violence
        if A==None or len(A)<=2:
            return 0
        count=0
        for i in range(0,len(A)-2,1):
            d=A[i+1]-A[i]
            for j in range(i+2,len(A),1):
                if A[j]-A[j-1]==d:
                    count+=1
                else:
                    break
        return count

    def numberOfArithmeticSlices3(self, A: list) -> int:  # dynamic programming
        dp = [0] * len(A)
        sum = 0
        for i in range(2, len(A), 1):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
                sum = sum + dp[i]
        return sum

if __name__=="__main__":
    n=[1, 2, 3, 4]
    so=Solution()
    a=so.numberOfArithmeticSlices3(n)
    print(a)