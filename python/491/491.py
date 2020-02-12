# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 0028 13:31
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 491.py
# @Software: PyCharm
# todo: need to learn
"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import copy
class Solution:
    def findSubsequences(self, nums: list) -> list: # time limit exceed
        def dfs(nums:list,index:int,res:list,path:list):
            # if the length >2, append to results
            if len(path) >=2 and path not in res:
                res.append(copy.deepcopy(path))
                # print(res)
            for i in range(index,len(nums)): # exist
                if not path or path[-1]<=nums[i]:
                    path+=[nums[i]]
                    dfs(nums,i+1,res,path)
                    path.pop()
            return res

        res=[] # save results to return
        path=[] # like the stack
        dfs(nums,0,res,path)
        return res
    def findSubsequences2(self, nums: list) -> list:
        res = []

        def dfs(start, tmp):
            dic = {}
            if len(tmp) > 1:
                res.append(tmp)
            for i in range(start, len(nums)):
                if dic.get(nums[i], 0):
                    continue

                if len(tmp) == 0 or nums[i] >= tmp[-1]:
                    dic[nums[i]] = 1
                    dfs(i + 1, tmp + [nums[i]])

        dfs(0, [])
        return res
    def findSubsequences3(self, nums: list) -> list: # time limit exceed
        """
                :type nums: List[int]
                :rtype: List[List[int]]
                """
        # 回溯法
        res = []

        def restore(nums, s):
            if not s in res and len(s) > 1:
                res.append(s)

            for i in range(len(nums)):
                if s and nums[i] < s[-1]:
                    return
                else:
                    restore(nums[i + 1:], s + [nums[i]])

        restore(nums, [])

        return res

if __name__=="__main__":
    s=[4, 6, 7, 7]
    so=Solution()
    a=so.findSubsequences3(s)
    print(a)