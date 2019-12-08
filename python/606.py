# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 0008 8:31
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 606.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            print(3333)
            return ""
        res=str(t.val)
        if t.left:
            res+="("
            res+=self.tree2str(t.left)
            res+=")"
            if t.right:
                res+="("
                res+=self.tree2str(t.right)
                res+=")"
        else:
            if t.right:
                res+="()("
                res+=self.tree2str(t.right)
                res+=")"
        return res

    def tree2str2(self, t: TreeNode) -> str:
        if t is None:
            return ""
        res=str(t.val)
        if not t.left and t.right:
            res+="()("+self.tree2str(t.right)+")"
        else:
            if t.left:
                res+="("+self.tree2str(t.left)+")"
            if t.right:
                res+="("+self.tree2str(t.right)+")"
        return res

if __name__=="__main__":
    t=TreeNode(1)
    t.left=TreeNode(2)
    t.right=TreeNode(3)
    t.left.left=TreeNode(None)
    t.left.right=TreeNode(4)

    so=Solution()
    a=so.tree2str2(t)
    print(a)