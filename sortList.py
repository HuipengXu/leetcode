# @Time    : 2019/4/9 8:44
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import random


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def quick_sort_c(head, tail):
            mid = partition(head, tail)
            if mid is None: return
            quick_sort_c(head, mid)
            quick_sort_c(mid.next, tail)

        def partition(head, tail):
            if head == tail or head.next == tail: return
            node = head
            length = 1
            while node.next != tail:
                node = node.next
                length += 1
            idx = random.randint(0, length - 1)
            i = j = mid = pivot = head
            for _ in range(idx):
                pivot = pivot.next
            pivot.val, node.val = node.val, pivot.val
            while i != tail:
                if i.val <= node.val:
                    i.val, j.val = j.val, i.val
                    mid = j
                    j = j.next
                i = i.next
            return mid

        quick_sort_c(head, None)
        return head

    def sortList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def quick_sort_c(head, tail):
            mid = partition(head, tail)
            if mid is None: return
            quick_sort_c(head, mid)
            quick_sort_c(mid.next, tail)

        def partition(head, tail):
            if head == tail or head.next == tail: return
            pivot, i, j = head.val, head.next, head
            while i != tail:
                if i.val < pivot:
                    j = j.next
                    i.val, j.val = j.val, i.val
                i = i.next
            head.val, j.val = j.val, head.val
            return j

        quick_sort_c(head, None)
        return head

    def sortList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def quick_sort_c(parent, head, tail):
            mid = partition(parent, head, tail)
            if mid is None: return
            quick_sort_c(parent, parent.next, mid)
            quick_sort_c(mid, mid.next, tail)

        def partition(parent, head, tail):
            if head == tail or head.next == tail: return
            mid = point = old_head = head
            flag = False
            while point.next != tail:
                if point.next.val < head.val:
                    new_head = point.next
                    point.next = point.next.next
                    new_head.next = old_head
                    old_head = new_head
                else:
                    if not flag:
                        mid = point
                        flag = True
                    point = point.next
            parent.next = old_head
            return mid

        tmp_head = ListNode(-1)
        tmp_head.next = head
        quick_sort_c(tmp_head, head, None)
        return tmp_head.next

    # 通过，以上快排版本都超出时间限制
    def sortList3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge_sort_c(parent, head, tail):
            if head == tail or head.next == tail: return
            fast = slow = head
            while fast != tail:
                if fast.next == tail:
                    break
                fast = fast.next.next
                slow = slow.next
            merge_sort_c(parent, head, slow)
            node = parent
            while node.next != slow:
                node = node.next
            merge_sort_c(node, slow, tail)
            merge(parent, parent.next, node.next, tail)

        def merge(parent, head, mid, tail):
            tmp_mid, tmp_parent = mid, parent
            while head != tmp_mid and mid != tail:
                if head.val < mid.val:
                    tmp_parent.next = head
                    tmp_parent = head
                    head = head.next
                else:
                    tmp_parent.next = mid
                    tmp_parent = mid
                    mid = mid.next
            if head == tmp_mid:
                tmp_parent.next = mid
            elif mid == tail:
                tmp_parent.next = head
                while tmp_parent.next != tmp_mid:
                    tmp_parent = tmp_parent.next
                tmp_parent.next = tail

        tmp_head = ListNode(-1)
        tmp_head.next = head
        merge_sort_c(tmp_head, head, None)
        return tmp_head.next

    def sortList4(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge_sort_c(head):
            if head == None: return
            if head.next == None: return head
            fast = slow = pre = head
            while fast != None and fast.next != None:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            # 分割链表
            pre.next = None
            l = merge_sort_c(head)
            r = merge_sort_c(slow)
            return merge(l, r)

        def merge(l, r):
            head = ListNode(-1)
            tmp_head = head
            while l != None and r != None:
                if l.val < r.val:
                    tmp_head.next = l
                    tmp_head = l
                    l = l.next
                else:
                    tmp_head.next = r
                    tmp_head = r
                    r = r.next
            if l == None:
                tmp_head.next = r
            else:
                tmp_head.next = l
            return head.next

        return merge_sort_c(head)


if __name__ == "__main__":
    head = ListNode(4)
    node = head
    for i in [2, 3, 1, 5]:
        node.next = ListNode(i)
        node = node.next
    s = Solution()
    sorted_head = s.sortList3(head)
