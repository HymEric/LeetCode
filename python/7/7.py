# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 0030 17:46
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 7.py
# @Software: PyCharm
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def reverse(self, x: int) -> int:
        flag = 1  # positive number
        if x < 0:
            flag = 0
            x = -x
        i = x
        j = 0
        sum = 0
        cnt = 0
        while (i != 0):
            j = i % 10
            sum = sum + 10 ** (len(str(i)) - 1) * j
            if flag==0:
                temp=-sum
            else:
                temp=sum
            if -2 ** 31 > temp or temp > 2 ** 31 - 1: # similar to prune
                return 0
            i = i // 10
            # print(sum)
            cnt += 1
        if flag == 0:
            sum = -sum
        if -2 ** 31 <= sum <= 2 ** 31 - 1:
            return sum
        else:
            return 0

if __name__=="__main__":
    n=0
    so=Solution()
    a=so.reverse(n)
    print(a)