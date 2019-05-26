# @Time    : 2019/5/24 21:02
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        length = 0
        while fast and fast.next:
            length += 1
            slow = slow.next
            fast = fast.next.next
        if fast:
            length = 2 * length + 1
        else:
            length = 2 * length
        if n >= length / 2:
            i, p = 0, head
            if length - n - 1 < 0: return head.next
        else:
            i, p = length // 2, slow
        while i < length - n - 1:
            p = p.next
            i += 1
        p.next = p.next.next
        return head

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
