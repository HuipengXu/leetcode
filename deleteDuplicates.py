# @Time    : 2019/6/14 8:08
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node:
            temp, pre = node.next, node
            while temp and temp.val == pre.val:
                pre, temp = temp, temp.next
            node.next, node = temp, temp
        return head

    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
