# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 0027 15:01
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 347.py
# @Software: PyCharm
"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        my_dicts=collections.Counter(nums)
        print(my_dicts)
        res=[]
        top_k=my_dicts.most_common(k)
        for item in top_k:
            res.append(item[0])
        return res
    def topKFrequent2(self, nums: list, k: int) -> list:
        dict_counts=collections.Counter(nums)
        # print(dict_counts.keys())
        # print(dict_counts.get)
        return heapq.nlargest(k,dict_counts,key=lambda x:dict_counts[x])
        # return heapq.nlargest(k,dict_counts.keys(),key=dict_counts.get)
    def topKFrequent3(self, nums: list, k: int) -> list:
        dicts=collections.Counter(nums)
        heap=[]
        for key,value in dicts.items(): # heapq里面默认小根堆，需要加负号
            heapq.heappush(heap,[-value,key])
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
if __name__=="__main__":
    nums = [1,1,1,2,2,3,4,4,4,4]
    k =2
    so=Solution()
    a=so.topKFrequent3(nums,k)
    print(a)