# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 0026 16:27
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 500.py
# @Software: PyCharm
"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

示例：

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
 

注意：

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keyboard-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def findWords(self, words: list) -> list:
        l1 = 'qwertyuiopQWERTYUIOP'
        l2 = 'asdfghjklASDFGHJKL'
        l3 = 'zxcvbnmZXCVBNM'
        l1,l2,l3=set(l1),set(l2),set(l3)
        res=[]
        for i in range(len(words)):
            s=set(words[i])
            if s&l1==s or s&l2==s or s&l3== s:
                res.append(words[i])
        return res
    def findWords2(self, words: list) -> list:
        l1 = 'qwertyuiop'
        l2 = 'asdfghjkl'
        l3 = 'zxcvbnm'
        l1,l2,l3=set(l1),set(l2),set(l3)
        res=[]
        for word in words:
            x=word.lower()
            setx=set(x)
            if setx<=l1 or setx<=l2 or setx<=l3:
                res.append(word)
        return res
if __name__=="__main__":
    s= ["Hello", "Alaska", "Dad", "Peace"]
    so=Solution()
    a=so.findWords2(s)
    print(a)