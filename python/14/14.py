# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 10:06
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 14.py
# @Software: PyCharm
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        n=len(strs)
        if n==0:
            return ""
        minLen=99999
        for i in range(n):
            if len(strs[i])<minLen:
                minLen=len(strs[i])
        # print(minLen)
        res=""
        for i in range(minLen):
            st=strs[0][i]
            flag=True
            for j in range(1,n):
                if strs[j][i]==st:
                    # print(strs[j][i])
                    continue
                else:
                    flag=False
                    break
            if flag==True:
                res=res+st
            else:
                break
        return res
    def longestCommonPrefix2(self, strs: list) -> str:
        res=""
        for i in zip(*strs): # https://blog.csdn.net/qq_31150463/article/details/84135708
            if len(set(i))==1:
                res=res+i[0]
            else:
                break
        return res
if __name__=="__main__":
    s= ["aa","aab"]
    so=Solution()
    a=so.longestCommonPrefix2(s)
    print(a)