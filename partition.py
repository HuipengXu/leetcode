# @Time    : 2019/6/3 19:07
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> Optional[ListNode]:
        if not head: return
        node = head
        pre = None
        while node and node.val < x:
            pre = node
            node = node.next
        lt_xs = []
        pre1 = node
        lt_x = node.next if node else None
        while lt_x:
            if lt_x.val < x:
                pre1.next = lt_x.next
                lt_x.next = None
                lt_xs.append(lt_x)
                lt_x = pre1.next
            else:
                pre1, lt_x = lt_x, lt_x.next
        if not lt_xs: return head
        if pre is None:
            head = lt_xs[0]
            node1 = head
            for n in lt_xs[1:]:
                node1.next = n
                node1 = n
            node1.next = node
        else:
            node1 = pre
            for n in lt_xs:
                node1.next = n
                node1 = n
            node1.next = node
        return head

    def partition1(self, head: ListNode, x: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        pre, node = dummy, head
        while node and node.val < x:
            pre, node = node, node.next
        part, ls_pre = node, node
        node = node.next if node else None
        while node:
            if node.val < x:
                ls_pre.next = node.next
                pre.next, pre = node, node
                node = ls_pre.next
            else:
                ls_pre, node = node, node.next
        pre.next = part
        return dummy.next

    def partition2(self, head: ListNode, x: int) -> Optional[ListNode]:
        before = ListNode(None)
        after = ListNode(None)
        node1, node2 = before, after
        while head:
            if head.val < x:
                node1.next, node1 = head, head
            else:
                node2.next, node2 = head, head
            head = head.next
        node1.next, node2.next = after.next, None
        return before.next


if __name__ == '__main__':
    nums = [1, 4, 3, 2, 5, 2]
    dummy = ListNode(-1)
    node = dummy
    for num in nums:
        node.next = ListNode(num)
        node = node.next
    s = Solution()
    print(s.partition2(dummy.next, 3))
