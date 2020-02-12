# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 0027 14:29
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 454.py
# @Software: PyCharm
"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class Solution:
    def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
        dicts=collections.Counter((a+b) for a in A for b in B)
        return sum(dicts.get(-(c+d),0) for c in C for d in D)
if __name__=="__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    so=Solution()
    a=so.fourSumCount(A,B,C,D)
    print(a)