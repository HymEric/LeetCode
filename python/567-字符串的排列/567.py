# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 0011 11:13
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 567.py
# @Software: PyCharm
"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def getHash(s:str):
            hashTable=dict()
            for i in s:
                if i not in hashTable:
                    hashTable[i]=0
                hashTable[i]+=1
            return hashTable
        lenS1=len(s1)
        lenS2=len(s2)
        lenDiff=lenS2-lenS1
        if lenDiff<0:
            return False

        head,tail=0,lenS1-1
        hashS1=getHash(s1)
        hashS2=getHash(s2[head:tail+1])
        while tail<lenS2:
            if hashS1==hashS2:
                return True
            tail+=1
            if tail==lenS2:
                break
            if s2[tail] not in hashS1:
                if tail+1+lenS1>=lenS2:
                    break
                else:
                    head=tail+1
                    tail=head+lenS1-1
                    hashS2=getHash(s2[head:tail+1])
            else:
                if s2[tail] not in hashS2:
                    hashS2[s2[tail]]=0
                hashS2[s2[tail]]+=1
                hashS2[s2[head]]-=1
                if hashS2[s2[head]]==0:  #这里需要注意的是，如果这里没有了这个数，则需要删除这个键值
                    del hashS2[s2[head]]
                head+=1
        return False
if __name__=="__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    so=Solution()
    a=so.checkInclusion(s1,s2)
    print(a)