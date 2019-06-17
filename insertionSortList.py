# @Time    : 2019/6/17 7:40
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        dummy = ListNode(-1)
        dummy.next = head
        cur, pre = head.next, head
        head.next = head.next.next

        while cur:
            node = dummy
            while node is not pre and node.next and node.next.val <= cur.val:
                node = node.next
            cur.next = node.next
            node.next = cur
            cur = pre.next
            while cur and cur.val >= pre.val:
                pre, cur = cur, cur.next
            if cur: pre.next = cur.next

        return dummy.next

    def insertionSortList1(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        dummy = ListNode(-1)
        dummy.next = head

        while head and head.next:
            if head.next.val >= head.val:
                head = head.next
                continue
            node = dummy
            while node.next.val <= head.next.val:
                node = node.next
            cur = head.next
            head.next = cur.next
            cur.next = node.next
            node.next = cur

        return dummy.next
