# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 0012 20:14
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 75.py
# @Software: PyCharm
"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def sortColors(self, nums: list) -> None: # heap
        """
        Do not return anything, modify nums in-place instead.
        """
        import heapq
        heap=[]
        heapq.heapify(heap)
        for i in range(len(nums)):
            heapq.heappush(heap,nums[i])
        for i in range(len(heap)):
            nums[i]=heapq.heappop(heap)
    def sortColors2(self, nums: list) -> None: # three pointer
        # 在p1左边的元素都是0，在p2右边的元素都是2
        curr,p1=0,0 # init
        p2=len(nums)-1
        while curr<=p2:
            if nums[curr]==0:
                nums[curr],nums[p1]=nums[p1],nums[curr]
                curr+=1
                p1+=1
            elif nums[curr]==2:
                nums[curr],nums[p2]=nums[p2],nums[curr]
                p2-=1
            elif nums[curr]==1:
                curr+=1

if __name__=="__main__":
    s1 =[2,0,2,1,1,0]
    so=Solution()
    so.sortColors2(s1)
    print(s1)