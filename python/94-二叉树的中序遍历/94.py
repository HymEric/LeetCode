# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 0008 14:42
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 94.py
# @Software: PyCharm
"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        res=[]
        def fun(root:TreeNode):
            if root == None:
                return
            fun(root.left)
            res.append(root.val)
            fun(root.right)
        fun(root)
        return res
    def inorderTraversal2(self, root: TreeNode) -> list:
        WHITE,GRAY=0,1
        res=[]
        stack=[(WHITE,root)]
        while stack:
            color,node=stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE,node.right))
                stack.append((GRAY,node))
                stack.append((WHITE,node.left))
            else:
                res.append(node.val)
        return res
    # other order by color method
    def preOrder(self, root: TreeNode) -> list:
        white,gray=0,1
        res=[]
        stack=[(white,root)]
        while stack:
            color,node=stack.pop()
            if node==None: continue
            if color==white: # 从小往上写，因为栈是先进后出
                stack.append((white,node.right)) # 3
                stack.append((white,node.left)) # 2
                stack.append((gray,node)) # 1
            else:
                res.append(node.val)
        return res
    def postOrder(self, root: TreeNode) -> list:
        white,gray=0,1
        res=[]
        stack=[(white,root)]
        while stack:
            color,node=stack.pop()
            if node is None: continue
            if color==white:
                stack.append((gray,node))
                stack.append((white,node.right))
                stack.append((white,node.left))
            else:
                res.append(node.val)
        return res
    def levelOrder(self, root: TreeNode) -> list:
        white,gray=0,1
        res=[]
        stack=[(white,root,0)]
        while stack:
            # print(stack.pop())
            color,node,level=stack.pop()
            if node == None: continue
            if color==white:
                stack.append((white,node.right,level+1))
                stack.append((white,node.left,level+1))
                stack.append((gray,node,level))
            else:
                if len(res)==level:
                    res.append([])
                res[level].append(node.val)
        return res
if __name__=="__main__":
    # [3,9,20,null,null,15,7]
    r=TreeNode(3)
    r.left=TreeNode(9)
    r.right=TreeNode(20)
    r.right.left=TreeNode(15)
    r.right.right=TreeNode(7)
    # r=None
    so=Solution()
    a=so.inorderTraversal2(r)
    print(a)
    print(so.preOrder(r))
    print(so.postOrder(r))
    print(so.levelOrder(r))