# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 0007 10:00
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 260.py
# @Software: PyCharm
"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class Solution:
    def singleNumber(self, nums: list) -> list:
        res=[]
        my_dicts=collections.Counter(nums)
        for key,value in my_dicts.items():
            if value==1:
                res.append(key)
        return res
    def singleNumber2(self, nums: list) -> list:
        # bitmask用于保存两个数中的不同数字，也就是出现奇数次的位
        bitmask=0
        for num in nums:
            bitmask=bitmask ^ num
        # 计算bitmask中最右边的1
        diff=bitmask & (-bitmask)
        x=0
        for num in nums:
            # 如果相与是0，则说明diff中的1在num中
            if num & diff:
                x=x^num
        return [x,bitmask^x]



if __name__=="__main__":
    n = [1,2,1,3,2,5]
    so=Solution()
    a=so.singleNumber2(n)
    print(a)