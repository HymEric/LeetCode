# -*- coding: utf-8 -*-
# @Time    : 2020/2/12 0012 17:10
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 142.py
# @Software: PyCharm
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。


 

进阶：
你是否可以不用额外空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode: # easy way using hash table
        hashTable=dict()
        while head!=None:
            if head in hashTable:
                return head
            else:
                hashTable[head]=1
                head=head.next
        return None

    def detectCycle2(self, head: ListNode) -> ListNode: # double pointer
        slow,fast=head,head # slow and fast pointer
        while True:
            if not fast or not fast.next:
                return
            fast,slow=fast.next.next,slow.next
            if fast==slow: # the first time encounter, when meet, fast pointer steps - slow ponter steps=(the steps of loop)*N (N=1,2,3)
                break
        fast=head
        while fast!=slow: # second time encounter
            fast,slow=fast.next,slow.next
        return fast

if __name__=="__main__":
    # head = [3, 2, 0, -4]
    # pos=1
    l=ListNode(3)
    l.next=ListNode(2)
    l.next.next=ListNode(0)
    l.next.next.next = ListNode(-4)
    l.next.next.next.next = l.next
    so=Solution()
    a=so.detectCycle2(l)
    if a:
        print(a.val)
    else:
        print('None')
    # while a:
    #     print(a.val)
    #     a=a.next