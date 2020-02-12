# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 0026 16:47
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 525.py
# @Software: PyCharm
"""
给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。

示例 1:

输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

注意: 给定的二进制数组的长度不会超过50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def findMaxLength(self, nums: list) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        cur_sum=0
        look_records={0:-1}
        res=0
        for i,num in enumerate(nums):
            cur_sum+=num
            if cur_sum in look_records:
                res=max(res,i-look_records[cur_sum])
            else:
                look_records[cur_sum]=i
        return res
    def findMaxLength2(self, nums: list) -> int:
        cnt=0
        res=0
        length=len(nums)
        arrs=[-2]*2*length+[-2]
        arrs[length]=-1
        for i,num in enumerate(nums):
            if num==0:
                cnt-=1
            elif num==1:
                cnt+=1
            if arrs[cnt+length]>=-1:
                res=max(res,i-arrs[cnt+length])
            else:
                arrs[cnt+length]=i
        return res

if __name__=="__main__":
    s= [0,1,0]
    so=Solution()
    a=so.findMaxLength(s)
    print(a)