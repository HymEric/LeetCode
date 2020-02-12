# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 0028 18:52
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 100.py
# @Software: PyCharm
"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # recurse
        def dfs( p: TreeNode, q: TreeNode):
            # print(p.val)
            # print(q.val)
            if p == None and q == None:
                return True
            if type(p) != type(q):
                return False
            if(p.val!=q.val):
                return False
            return dfs(p.left,q.left) and dfs(p.right,q.right)
        return dfs(p,q)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        import collections
        def check(p,q):
            if p==None and q==None:
                return True
            if type(p)!=type(q):
                return False
            if p.val!=q.val:
                return False
            return True
        deq=collections.deque([(p,q),])
        while deq:
            p,q=deq.popleft()
            if not check(p,q):
                return False
            if p:
                deq.append((p.left,q.left))
                deq.append((p.right,q.right))
        return True

if __name__=="__main__":
    p=TreeNode(1)
    p.left=TreeNode(2)
    # p.right=TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    so=Solution()
    a=so.isSameTree2(p,q)
    print(a)