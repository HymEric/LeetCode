# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 0028 12:00
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 290.py
# @Software: PyCharm
"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。   

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def wordPattern(self, pattern:str, str: str) -> bool:
        res=str.split(' ')
        # print(map(pattern.index,pattern))
        # print(tuple(map(pattern.index,pattern)))
        a=list(map(pattern.index,pattern))
        b=list(map(res.index,res))
        # print(a)
        # print(b)
        return a==b

    def wordPattern2(self, pattern: str, str: str) -> bool:
        str=str.split(' ')
        a=[]
        b=[]
        length=len(pattern)
        if len(str)!=length:
            return False
        for i in range(length):
            a.append(pattern.index(pattern[i]))
            b.append(str.index(str[i]))
        # print(a)
        # print(b)
        return a==b

if __name__=="__main__":
    pattern = "aaa"
    str ="aa aa aa aa"
    so=Solution()
    a=so.wordPattern2(pattern,str)
    print(a)