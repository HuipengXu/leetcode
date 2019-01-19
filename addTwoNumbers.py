# @Time    : 2019/1/19 9:11
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    2. 两数相加
    """

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carrying = 0
        rl = ListNode(0)
        rl_node = rl
        while l1 and l2:
            carrying, val = divmod(l1.val + l2.val + carrying, 10)
            l1 = l1.next
            l2 = l2.next
            rl_node.next = ListNode(val)
            rl_node = rl_node.next
        if l1 or l2:
            l3 = l2 if not l1 else l1
            while l3:
                carrying, val = divmod(l3.val + carrying, 10)
                l3 = l3.next
                rl_node.next = ListNode(val)
                rl_node = rl_node.next
        if carrying == 1:
            rl_node.next = ListNode(carrying)
        return rl.next
