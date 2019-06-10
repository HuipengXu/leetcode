# @Time    : 2019/6/10 7:43
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> Optional[TreeNode]:
        if not head: return

        def get_mid(head: ListNode) -> ListNode:
            slow = fast = head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            if pre: pre.next = None
            return slow

        mid = get_mid(head)
        left = head if head is not mid else None
        right = mid.next
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root
