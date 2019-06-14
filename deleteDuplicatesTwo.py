# @Time    : 2019/6/14 9:03
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        node, pre, flag = head, dummy, True
        while node:
            while node and node.next and node.val == node.next.val:
                node = node.next
                flag = False
            if flag:
                pre.next, pre = node, node
                node = node.next
            else:
                node, flag = node.next, True
        if pre.next: pre.next = None
        return dummy.next

    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(None)
        dummy.next = head
        slow, fast = dummy, dummy.next
        while fast:
            while fast.next and slow.next.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow = fast
            else:
                slow.next = fast.next
            fast = fast.next
        return dummy.next
