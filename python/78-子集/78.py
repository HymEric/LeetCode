# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 0008 9:53
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 78.py
# @Software: PyCharm
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import itertools
class Solution:
    def subsets(self, nums:list) ->list:
        res=[]
        n=len(nums)
        def helper(i,tmp):
            res.append(tmp)
            # print(res)
            for j in range(i,n):
                helper(j+1,tmp+[nums[j]])
        helper(0,[])
        return res
    def subsets2(self, nums:list) ->list: # api
        res=[]
        for i in range(0,len(nums)+1):
            for iter in itertools.combinations(nums,i):
                res.append(list(iter))
        return res
    def subsets3(self, nums:list) ->list:
        res=[[]]
        for i in nums:
            for j in res:
                res=res+[[i]+j]
            print(res)
        return res
    def subsets4(self, nums:list) ->list: # bit
        size=len(nums)
        n=1<<size
        res=[]
        for i in range(n):
            cur=[]
            for j in range(size):
                print(bin(i>>j))
                if i>>j &1: # 根据i掩码，判断当前第j个数是否要
                    cur.append(nums[j])
            res.append(cur)
        return res


if __name__=="__main__":
    n =[1,2,3]
    so=Solution()
    a=so.subsets4(n)
    print(a)