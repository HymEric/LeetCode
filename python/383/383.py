# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 9:21
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 383.py
# @Software: PyCharm
"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ransom-note
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
C++题解：
此题最难的就是读懂题，此题的意思是用后面字符串的字符是否可以组成前面一个字符，所以此题只需要判断后面各个字符的总数是否大于前面字符的即可，
这又成了一个映射问题，字符映射个数，所以我们又可以用map来解决问题，只需要先遍历后面字符串统计所有字符出现的次数，然后在遍历前面一个字符串，
然后每遍历一个字符串就减去1再判断是否小于0即可。遇到有映射关系的题就要优先考虑使用map
python：可用collection
"""
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(collections.Counter(ransomNote))
        print(collections.Counter(magazine))
        print(collections.Counter(magazine) & collections.Counter(ransomNote))
        # return bool(collections.Counter(magazine)-collections.Counter(ransomNote))
        return (collections.Counter(magazine) & collections.Counter(ransomNote)) == collections.Counter(ransomNote)

if __name__=="__main__":
    s="aa"
    b="aab"
    so=Solution()
    a=so.canConstruct(s,b)
    print(a)