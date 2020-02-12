# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 0011 16:16
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 148.py
# @Software: PyCharm
"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid=self.getMid(head)
        left=self.sortList(head)
        right=self.sortList(mid)
        return self.merge(left,right)
    def getMid(self,head:ListNode):
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        return mid
    def merge(self,left:ListNode,right:ListNode):
        res=ListNode(-1)
        p=res
        while left and right:
            if left.val <=right.val:
                p.next=left
                left=left.next
            else:
                p.next=right
                right=right.next
            p=p.next
            # p.next=None # delete the original link in left and right
        if left:
            p.next=left
        if right:
            p.next=right
        return res.next


    def sortList2(self, head: ListNode) -> ListNode: # 优先队列揭解法(小根堆也一样）
        import queue
        ptr=head
        p_queue=queue.PriorityQueue()
        while ptr!=None:
            p_queue.put(ptr.val)
            ptr=ptr.next
        ptr=head
        while not p_queue.empty():
            ptr.val=p_queue.get()
            ptr=ptr.next
        return head


if __name__=="__main__":
    # head = [3, 2, 0, -4]
    # pos=1
    l=ListNode(3)
    l.next=ListNode(2)
    l.next.next=ListNode(0)
    l.next.next.next = ListNode(-4)
    # l.next.next.next.next = l.next
    so=Solution()
    a=so.sortList(l)
    while a:
        print(a.val)
        a=a.next