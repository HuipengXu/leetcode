# @Time    : 2019/6/29 9:24
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next, pre = head, dummy
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return dummy.next

    def removeElements1(self, head: ListNode, val: int) -> ListNode:
        if head: head.next = self.removeElements1(head.next, val)
        return head.next if head and head.val == val else head
