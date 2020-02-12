# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 0031 12:04
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 462.py
# @Software: PyCharm
"""
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math
class Solution:
    def minMoves2(self, nums: list) -> int:
        nums.sort()
        mid=nums[len(nums)//2]
        res=0
        for i in range(len(nums)):
            res+=abs(nums[i]-mid)
        return res
    def minMoves2_2(self, nums: list) -> int:
        length=len(nums)
        if length<=1:
            return 0
        nums.sort()
        mid=length//2
        if length%2==0:
            return sum(nums[mid:])-sum(nums[0:mid])
        else:
            return sum(nums[mid+1:])-sum(nums[:mid])

if __name__=="__main__":
    n=[1,2]
    so=Solution()
    a=so.minMoves2_2(n)
    print(a)