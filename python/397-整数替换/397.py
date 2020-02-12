# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 0008 11:02
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 397.py
# @Software: PyCharm
"""
给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

示例 1:

输入:
8

输出:
3

解释:
8 -> 4 -> 2 -> 1
示例 2:

输入:
7

输出:
4

解释:
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        step=0
        while(n!=1):
            if n%2==0:
                n=n>>1
            else:
                if n==3 or bin(n).endswith('01'): # or n & 2==1
                    n-=1
                else:
                    n+=1
            step+=1
        return step
    def integerReplacement2(self, n: int) -> int:
        if n==1:
            return 0
        elif n&1==0:
            return 1+self.integerReplacement2(n//2)
        else:
            return 1+min(self.integerReplacement2(n-1),self.integerReplacement2(n+1))

if __name__=="__main__":
    n =65535
    so=Solution()
    a=so.integerReplacement2(n)
    print(a)