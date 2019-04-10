# @Time    : 2019/4/10 10:02
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList0(self, head: ListNode) -> ListNode:
        pre = None
        while head != None:
            next_ = head.next
            head.next = pre
            pre = head
            head = next_
        return pre

    def reverseList1(self, head: ListNode) -> ListNode:
        def recur(parent: Optional[ListNode], node: ListNode):
            if node == None: return None
            if node.next == None:
                node.next = parent
                return node
            new_head = recur(node, node.next)
            node.next = parent
            return new_head

        return recur(None, head)
