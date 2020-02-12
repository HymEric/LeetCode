# -*- coding: utf-8 -*-
# @Time    : 2020/1/25 0025 19:55
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 345.py
# @Software: PyCharm
"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        # double pointer
        arr=list(s)
        left,right=0,len(arr)-1 # p1,p2
        vowels=['a','e','i','o','u','A','E','I','O','U']
        while left<right:
            while arr[left] not in vowels and left<right:
                left+=1
            while arr[right] not in vowels and left<right:
                right-=1
            if left<right:
                arr[right],arr[left]=arr[left],arr[right]
                left+=1
                right-=1
        return ''.join(arr)

if __name__=="__main__":
    s= 'leetcode'
    so=Solution()
    a=so.reverseVowels(s)
    print(a)