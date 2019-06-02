# @Time    : 2019/6/2 14:27
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> Optional[ListNode]:
        if not head: return None
        slow = fast = head
        length = 0
        while fast and fast.next:
            length += 1
            slow = slow.next
            if not fast.next.next:
                tail = fast.next
            fast = fast.next.next
        if fast: tail = fast
        length = 2 * length + 1 if fast else 2 * length
        k %= length
        node = head
        for _ in range(length - k - 1):
            node = node.next
        tail.next = head
        head = node.next
        node.next = None
        return head
