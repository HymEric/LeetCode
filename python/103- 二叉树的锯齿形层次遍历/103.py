# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 0005 9:46
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 103.py
# @Software: PyCharm
"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        res=[]
        if not root:
            return res
        def fun(root:TreeNode,level):
            if len(res)==level:
                res.append([])
            res[level].append(root.val)

            if root.left:
                fun(root.left,level+1)
            if root.right:
                fun(root.right,level+1)
        fun(root,0)
        for level in range(len(res)):
            if level%2==1:
                res[level].reverse()
        return res
    def zigzagLevelOrder2(self, root: TreeNode) -> list:
        res=[]
        if not root:
            return res
        queue=collections.deque()
        queue.appendleft(root)
        level=0

        while queue:
            length_level=len(queue)
            res.append([])
            for i in range(length_level):
                node=queue.pop()
                if level%2==0:
                    res[level].append(node.val)
                else:
                    res[level].insert(0,node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            level+=1
        return res
    def zigzagLevelOrder3(self, root: TreeNode) -> list:
        res=[]
        if not root:
            return res
        def fun(root:TreeNode,level):
            if len(res)==level:
                res.append([])
            if level%2==0:
                res[level].append(root.val)
            else:
                res[level].insert(0,root.val)
            if root.left:
                fun(root.left,level+1)
            if root.right:
                fun(root.right,level+1)
        fun(root,0)
        return res

if __name__=="__main__":
    # [1,2,3,4,null,null,5]
    r=TreeNode(1)
    r.left=TreeNode(2)
    r.right=TreeNode(3)
    r.left.left=TreeNode(4)
    # r.right.left=TreeNode(15)
    r.right.right=TreeNode(5)
    # r=None
    so=Solution()
    a=so.zigzagLevelOrder3(r)
    print(a)
