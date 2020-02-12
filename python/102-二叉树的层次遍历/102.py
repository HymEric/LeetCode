# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 0004 11:23
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 102.py
# @Software: PyCharm
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
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
    def levelOrder(self, root: TreeNode) -> list: # time limited
        if not root:
            return None
        res=[] # results
        dequeue=collections.deque()
        dequeue.appendleft([root,root.val])
        dequeue.appendleft([root,0])

        temp=[]
        while dequeue:
            Tree,value=dequeue.pop()
            if value==0:
                res.append(temp)
                # print(res)
                if len(dequeue)>=1:
                    dequeue.appendleft([Tree,0])
                temp=[]
            else:
                temp.append(value)
                if Tree.left:
                    dequeue.appendleft([Tree.left,Tree.left.val])
                if Tree.right:
                    dequeue.appendleft([Tree.right,Tree.right.val])
        return res
    def levelOrder2(self, root: TreeNode) -> list: # speed is fast
        levels=[] # results
        if not root:
            return levels
        def helper(node,level):
            # start the current level
            if len(levels)==level:
                levels.append([])
            levels[level].append(node.val)

            # recursive
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
        helper(root,0)
        return levels
    def levelOrder3(self, root: TreeNode) -> list: # speed is slow
        res=[]
        if not root:
            return
        queue=collections.deque()
        queue.appendleft([root,0])
        while queue:
            node,level=queue.pop()
            if len(res)==level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.appendleft([node.left,level+1])
            if node.right:
                queue.appendleft([node.right,level+1])
        return res
    def levelOrder4(self, root: TreeNode) -> list:
        levels=[]
        if not root:
            return levels
        level=0
        queue=collections.deque([root,])
        while queue:
            levels.append([])
            level_length=len(queue)
            for i in range(level_length):
                node=queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return levels
if __name__=="__main__":
    # [3,9,20,null,null,15,7]
    r=TreeNode(3)
    r.left=TreeNode(9)
    # r.right=TreeNode(20)
    # r.right.left=TreeNode(15)
    # r.right.right=TreeNode(7)
    # r=None
    so=Solution()
    a=so.levelOrder4(r)
    print(a)