# @Time    : 2019/6/12 12:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> Optional[ListNode]:
        if not head: return
        dummy = ListNode(-1)
        dummy.next = head
        cnt, pre = 1, dummy
        while cnt < m:
            pre, head = head, head.next
            cnt += 1
        point_m = pre
        point_n = head
        while cnt <= n:
            tmp = head.next
            head.next = pre
            pre, head = head, tmp
            cnt += 1
        point_m.next = pre
        point_n.next = head
        return dummy.next

    def reverseBetween1(self, head: ListNode, m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        for _ in range(1, m):
            pre = pre.next
        head = pre.next
        for _ in range(m, n):
            next_ = head.next
            head.next = next_.next
            next_.next = pre.next
            pre.next = next_
        return dummy.next
