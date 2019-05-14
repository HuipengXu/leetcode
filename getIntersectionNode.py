# @Time    : 2019/4/10 8:54
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode0(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def get_length(head):
            length = 0
            while head != None:
                head = head.next
                length += 1
            return length

        length_a = get_length(headA)
        length_b = get_length(headB)
        if length_a - length_b >= 0:
            for _ in range(length_a - length_b):
                headA = headA.next
        else:
            for _ in range(length_b - length_a):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        if headA == None:
            return None
        else:
            return headA

    # 实际上当链表的长度不一致时，两种方法的时间复杂度一致，上面的空间稍微占用多一点；
    # 一致时，下面的方法省略了计算长度的循环。下面的写法很巧妙，当长度不一致时，进行交替遍历，
    # 这样在交替之后便实现了链表的尾对齐，相当于进行上面的最后一个 while 循环
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
