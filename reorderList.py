# @Time    : 2019/6/17 9:50
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = [slow] if not fast else []
        while slow.next:
            second_half.append(slow.next)
            slow = slow.next
        node = head
        while second_half:
            tmp = node.next
            last = second_half.pop()
            node.next, last.next = last, tmp
            node = tmp
        node.next = None

    def reorderList1(self, head: ListNode) -> None:
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        # 断链
        if fast:
            second_head, slow.next = slow.next, None
        else:
            pre.next, second_head = None, slow
        # 反转
        pre = None
        while second_head:
            tmp = second_head.next
            second_head.next = pre
            pre, second_head = second_head, tmp
        # 重组
        node = head
        while pre:
            tmp1 = node.next
            tmp2 = pre.next
            node.next = pre
            pre.next = tmp1
            node, pre = tmp1, tmp2
