# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 0017 19:24
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 616.py
# @Software: PyCharm

"""
LeetCode 616. Add Bold Tag in String
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b>
to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together
by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
"""

class Solution:
    def addBold(self,s:str,dicts:list)->str:
        n=len(s) # length of s
        is_bold=[False]*n # define a same length list to record whether the i-th element is right for problem
        end=0
        res=""
        for i in range(n):
            for word in dicts:
                length=len(word)
                if i+length<=n and s[i:i+length]==word:
                    end=max(end,i+length)
            is_bold[i]=end>i
        # print(is_bold)
        k=0
        while(k<n):
            if is_bold[k] is False:
                res.join(s[k])
                k+=1
                continue
            j=k
            while(j<n and is_bold[j]):
                j+=1
            res+="<b>"+s[k:j-k]+"</b>"
            k=j-1
            k+=1
            # break
        return res

if __name__=="__main__":
    s="aaabbccfre"
    dicts=["aaa","aabb","bc"]
    so=Solution()
    a=so.addBold(s,dicts)
    print(a)