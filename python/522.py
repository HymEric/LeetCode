# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 0008 9:15
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 522.py
# @Software: PyCharm
import collections

class Solution:
    def findLUSlength(self, strs: list) -> int:
        strs.sort(key=lambda x: -len(x))
        print(strs)
        d = collections.defaultdict(int)
        for i in strs:
            d[i] += 1

        def f(a, b):
            k = 0
            for c in a:
                j = b.find(c, k)
                if j == -1:
                    return False
                k = j + 1
            return True

        for i in d:
            if d[i] == 1:
                flag = True
                for j in d:
                    print(i,j)
                    if j == i:  # 碰到自己时不能直接break，因为同长度的可能还有其他词
                        continue
                    elif f(i, j):  # 判断子序列. i 是否在j里面
                        flag = False
                        break
                if flag:  # 如果在比自己长的词里面，没有找到子序列，那就输出自己的长度
                    return len(i)

        return -1

    def findLUSlength2(self, strs: list) -> int:
        # 有个东西要理解，有很多种情况，就是如果strs中的每个字符串长度都一样，要么返回值是字符串的长度，要么是-1
        # 如果里面有一个字符串都大于其余的字符串长度，则返回值就是这个最大的长度
        # 如果有好几部分，每一部分的字符串长度一样，分情况会很麻烦，所以不能简单的分情况讨论最大长度或者相同长度
        strs.sort(key=lambda x:-len(x))
        dic=collections.defaultdict(int)
        for str in strs:
            dic[str]+=1
        # a是否是b的子序列
        def fun(a,b):
            k=0
            for a_sub in a:
                t=b.find(a_sub,k)
                if t==-1:
                    return False
                k=t+1
            return True
        # 遍历字典
        for dic_sub in dic:
            # 不等于1的话说明有重复，肯定不符合题意
            if dic[dic_sub]==1:
                flag=True
                for j in dic:
                    if j==dic_sub: # 如果j和dic_sub相等,本身
                        continue
                    if len(j)<len(dic_sub): # 后面的字符串都小于当前的字符串
                        break
                    if fun(dic_sub,j): # 如果dic_sub是j的子串，这个条件只在dic_sub和j的长度相等的时候才触发
                        flag=False # 作为重新选择基准dic_sub的标志
                        break
                if flag: # 如果成立，则说明当前基准dic_sub就是最大的特殊序列，输出其长度
                    return len(dic_sub)
        return -1
    # def findLUSlength3(self, strs: list) -> int:
    #     strs.sort(key=lambda x:-len(x))
    #     strs_dict = collections.defaultdict(int)
    #     for str in strs:
    #         strs_dict[str] += 1
    #
    #     head_str_len=len(strs[0])
    #     # flag_same=False # 记录strs是否有重复的字符串
    #     flag_head=True # 记录是否strs[1:]都小于head的长度
    #     for i in range(1,len(strs)):
    #         if len(strs[i])>=head_str_len:
    #             flag_head=False
    #     if flag_head:
    #         return head_str_len
    #
    #         if strs_dict[str]>=2:
    #             return -1
    #     return len(strs[0])


if __name__=="__main__":
    l=["aabbcc", "aabbcc","cb"]
    so=Solution()
    a=so.findLUSlength2(l)
    print(a)
