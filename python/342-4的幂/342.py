# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 0006 11:11
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 342.py
# @Software: PyCharm
"""
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-four
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        for i in range(0,32+1,2):
            # print(i << i)
            if 1<<i==num:
                return True
        return False
    def isPowerOfFour2(self, num: int) -> bool: # naive
        if num<=0:
            return False
        while num%4==0:
            num/=4
        return num==1
    def isPowerOfFour3(self, num: int) -> bool: # math
        import math
        return num>0 and math.log(num,2)%2==0
    def isPowerOfFour4(self, num: int) -> bool:
        return num>0 and num & (num-1) ==0 and num & 0xaaaaaaaa==0

if __name__=="__main__":
    n = 262144
    so=Solution()
    a=so.isPowerOfFour4(n)
    print(a)