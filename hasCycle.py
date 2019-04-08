# @Time    : 2019/4/8 15:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        point1 = point2 = head
        while point1 and point2:
            point1 = point1.next
            point2 = point2.next
            if point2:
                point2 = point2.next
            else:
                return False
            if point1 == point2: return True
        return False
