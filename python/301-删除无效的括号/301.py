# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 0005 10:17
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 301.py
# @Software: PyCharm
"""
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> list: # easy way
        def isvalid(s:str): # if s is valid
            l_minus_r=0
            for i in range(len(s)):
                if s[i]=='(':
                    l_minus_r+=1
                elif s[i]==')':
                    l_minus_r-=1
                    if l_minus_r<0:
                        return False # invlid
            return l_minus_r==0 # valid
        level={s} # init
        while True:
            valid=list(filter(isvalid,level))
            if valid:
                return valid
            # level={s[:i]+s[i+1:] for s in level for i in range(len(s)) if s[i] in '()'}
            temp=set()
            for s in level:
                for i in range(len(s)):
                    if s[i] in '()':
                        temp=temp|{s[:i]+s[i+1:]}
            level=temp
    def removeInvalidParentheses2(self, s: str) -> list: # BFS
        res=set() # results
        rmL= 0 # the remove number of left parentheses
        rmR=0 # the remove number of right parentheses
        for a in s: # based on the parentheses number
            if a=='(':
                rmL+=1
            elif a==')':
                if rmL!=0:
                    rmL-=1
                else:
                    rmR+=1
        # if the s is valid
        def isValid(s:str):
            l_minus_r=0
            for a in s:
                if a =='(':
                    l_minus_r+=1
                elif a==')':
                    l_minus_r-=1
                    if l_minus_r<0:
                        return False
            return l_minus_r==0
        queue=collections.deque([(s,rmL,rmR)]) # 记录此时的s和需要删除的左括号和右括号
        visited=set()
        visited.add((s,rmL,rmR))
        while queue:
            temp_s,left_p,right_p=queue.pop()
            print(temp_s)
            # 输出条件
            if left_p==0 and right_p ==0 and isValid(temp_s):
                res.add(temp_s)
            for i in range(len(temp_s)):
                # 如果当前是字母
                if temp_s[i] not in '()':
                    continue
                if temp_s[i]=='(' and left_p>0:
                    t=temp_s[:i]+temp_s[i+1:]
                    # queue.appendleft((t, left_p - 1, right_p))
                    if (t,left_p-1,right_p) not in visited: # 访问过的，有可能删除符号有相同的结果，这里相当于剪枝，删去之后相同的结果只需要判定一次
                        queue.appendleft((t,left_p-1,right_p))
                        visited.add((t,left_p-1,right_p))
                if temp_s[i]==')' and right_p>0:
                    t=temp_s[:i]+temp_s[i+1:]
                    # queue.appendleft((t, left_p, right_p - 1))
                    if (t,left_p,right_p-1) not in visited:
                        queue.appendleft((t,left_p,right_p-1))
                        visited.add((t,left_p,right_p-1))
        return list(res)
    def removeInvalidParentheses3(self, s: str) -> list: # DFS
        # 计算字符串最长的有效括号的长度
        def longestValdParentheses(s:str):
            res = 0
            stack = []
            for a in s:
                if a == '(':
                    stack.append("(")
                elif a == ")":
                    if stack:
                        res += 2
                        stack.pop()
            return res
        # left_p,left_r是最长的有效括号的长度的一半，还需要这么些的括号，放tmp里面
        # open表示左右括号抵消多少,有一个（就要有一个）
        def helper(s:str,left_p,right_p,open,tmp):
            #当小于0 都不满足条件
            if left_p<0 or right_p<0 or open<0:
                return
            # s剩余的括号不够组成的
            if s.count('(')<left_p or s.count(')')<right_p:
                return
            if not s:
                if left_p==0 and right_p==0 and open==0:
                    res.add(tmp)
                return
            if s[0]=='(':
                # use "("
                helper(s[1:],left_p-1,right_p,open+1,tmp+"(")
                # not use"("
                helper(s[1:],left_p,right_p,open,tmp)
            elif s[0]==")":
                # use ")"
                helper(s[1:],left_p,right_p-1,open-1,tmp+')')
                # not use ")"
                helper(s[1:],left_p,right_p,open,tmp)
            else:
                helper(s[1:],left_p,right_p,open,tmp+s[0])

        l=longestValdParentheses(s)
        res=set()
        helper(s,l//2,l//2,0,"")
        return list(res)

if __name__=="__main__":
    n ="(a)())()"
    so=Solution()
    a=so.removeInvalidParentheses3(n)
    print(a)