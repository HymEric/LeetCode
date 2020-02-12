# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 0010 10:18
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 456.py
# @Software: PyCharm
"""
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

注意：n 的值小于15000。

示例1:

输入: [1, 2, 3, 4]

输出: False

解释: 序列中不存在132模式的子序列。
示例 2:

输入: [3, 1, 4, 2]

输出: True

解释: 序列中有 1 个132模式的子序列： [1, 4, 2].
示例 3:

输入: [-1, 3, 2, 0]

输出: True

解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import itertools
class Solution:
    def find132pattern(self, nums: list) -> bool:
        subs=itertools.combinations(nums,3)
        # print(list(subs))
        for iter in list(subs):
            if iter[1]>iter[2] and iter[0]<iter[2]:
                return True
        return False

    def find132pattern2(self, nums: list) -> bool:
        min_num=float('inf')
        for j in range(len(nums)):
            min_num=min(min_num,nums[j])
            if min_num==nums[j]: continue
            for k in range(len(nums)-1,j,-1):
                if nums[k]>min_num and nums[j]>nums[k]:
                    return True
        return False
    def find132pattern3(self, nums: list) -> bool:
        # 先在min_pre中保存i之前做小的数作为Xi,使用栈保存Xk,从nums右边遍历，
        # 如果nums[k]>min_pre[k]就说明k之前有一个数小于nums[k]，成立Xi<Xk，之后把候补的Xk放入栈,如果nums[k]==min_pre[k]，continue
        # 但是在放入栈之前需要检查，有contunue的时候可能栈顶元素小于等于min_pre[k],先检查栈顶元素是否小于等于min_pre[k]
        # 如果小于等于则pop，之后检查栈顶元素是否小于nums[k]（也就是Xj）,成立则返回True，最后入栈
        # 遍历完之后还没有返回True，就返回False
        length=len(nums)
        if length<3:
            return False
        min_pre=[nums[0]]
        # min_pre=[]
        for i in range(1,length):
            min_pre.append(min(nums[i],min_pre[-1]))
        stack=[]
        for k in range(length-1,-1,-1):
            if nums[k]>min_pre[k]:
                while stack and stack[-1]<=min_pre[k]:
                    stack.pop()
                if stack:
                    if stack[-1]<nums[k]:
                        return True
                stack.append(nums[k])

            elif nums[k]==min_pre[k]:
                continue
        return False

if __name__=="__main__":
    n =[-1,1,2,2,5,1,3]
    so=Solution()
    a=so.find132pattern3(n)
    print(a)