# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 9:54
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 257.py
# @Software: PyCharm
"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import copy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        if root==None:
            return None
        path=""
        res=[]

        def dfs(p:TreeNode,res,path:str):
            if path == "":
                path = str(p.val)
            else:
                path = path + '->' + str(p.val)
            if p.left==None and p.right==None and path not in res:
                res.append(copy.deepcopy(path))
            if p.left!=None:
                dfs(p.left, res,path)
            if p.right!=None:
                dfs(p.right, res, path)
            # if p.left!=None and p.right!=None:
            #     dfs(p.left,res,path)
            #     dfs(p.right,res,path)
        dfs(root,res,path)
        return res
    def binaryTreePaths2(self, root: TreeNode) -> list:
        paths=[]

        def construct_paths(root:TreeNode,path:str):
            if root:
                path=path+str(root.val) #
                if not root.left and not root.right: # leaf
                    paths.append(path)
                else: # not leaf, continue to recurse
                    path=path+'->'
                    construct_paths(root.left,path)
                    construct_paths(root.right,path)

        construct_paths(root, "")
        return paths
    def binaryTreePaths3(self, root: TreeNode) -> list:
        import collections
        paths=[]
        if root:
            deque = collections.deque([(root, str(root.val)), ])
            while deque:
                node, path = deque.pop()
                if not node.left and not node.right:
                    paths.append(path)
                if node.left:
                    deque.append((node.left, path + '->' + str(node.left.val)))
                if node.right:
                    deque.append((node.right, path + '->' + str(node.right.val)))
            return paths
if __name__=="__main__":
    p=TreeNode(1)
    p.left=TreeNode(2)
    p.right=TreeNode(3)
    p.left.right=TreeNode(5)
    # q = TreeNode(1)
    # q.left = TreeNode(2)
    # q.right = TreeNode(3)
    so=Solution()
    a=so.binaryTreePaths3(p)
    print(a)