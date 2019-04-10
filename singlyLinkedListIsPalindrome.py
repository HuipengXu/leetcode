# @Time    : 2019/4/10 11:20
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None: return True
        fast = slow = head
        pre = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            next_ = slow.next
            slow.next = pre
            pre = slow
            slow = next_
        if fast != None:
            slow = slow.next
        while pre and pre.val == slow.val:
            pre = pre.next
            slow = slow.next
        if pre == None:
            return True
        else:
            return False
