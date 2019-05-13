# @Time    : 2019/5/13 21:22
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        if slow != fast: return None
        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        return p

    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        node = head
        while node not in nodes and node:
            nodes.add(node)
            node = node.next
        return node
