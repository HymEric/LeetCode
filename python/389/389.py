# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 0027 14:21
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 389.py
# @Software: PyCharm
"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=collections.Counter(s)
        t=collections.Counter(t)
        res=t-s
        return ''.join(res)

if __name__=="__main__":
    s = "abcd"
    t = "abcde"
    so=Solution()
    a=so.findTheDifference(s,t)
    print(a)