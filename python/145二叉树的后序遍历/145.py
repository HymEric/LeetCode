# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 0010 10:07
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 145.py
# @Software: PyCharm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        white,gray=0,1
        res=[]
        stack=[(white,root)]
        while stack:
            color,node=stack.pop()
            if node==None:
                continue
            if color==white:
                stack.append((gray,node))
                stack.append((white,node.right))
                stack.append((white,node.left))
            else:
                res.append(node.val)
        return res