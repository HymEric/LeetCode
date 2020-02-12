# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 0011 12:47
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 125.py
# @Software: PyCharm
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        numbers = '1234567890'
        letters ='qwertyuiopasdfghjklzxcvbnm'
        s=s.lower()
        s_new=""
        for x in s:
            if (x in numbers) or (x in letters):
                s_new=s_new+x
        # print(s_new)
        if s_new=="":
            return True
        p1=0
        p2=len(s_new)-1
        while p1<=p2:
            if s_new[p1]==s_new[p2]:
                p1+=1
                p2-=1
                continue
            else:
                return False
        return True

if __name__=="__main__":
    s1 ="aa"
    so=Solution()
    a=so.isPalindrome(s1)
    print(a)