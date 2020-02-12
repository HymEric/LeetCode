# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 0030 16:56
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 400.py
# @Software: PyCharm
"""
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32为整形范围内 ( n < 2^31)。

示例 1:

输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nth-digit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        # regular
        base=9
        current_sum=base
        previous_sum=0
        for i in range(1,100000):
            if n<=current_sum: # when previous_sum<n<=current_sum
                div,mod=divmod(n-previous_sum-1,i)
                num=10**(i-1)+div # the answer str is in the num
                return str(num)[mod] # the mod-th str in str(num)
            base=9*(10**i)*(i+1)
            previous_sum=current_sum
            current_sum+=base

if __name__=="__main__":
    n=999
    so=Solution()
    a=so.findNthDigit(n)
    print(a)