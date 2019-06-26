# @Time    : 2019/6/26 9:19
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        fast, length = head, 0
        while fast and fast.next:
            length += 1
            fast = fast.next.next
        if fast:
            length = 2 * length + 1
        else:
            length *= 2
        i, pre, node = 0, dummy, head
        for j in range(k, length, k):
            for _ in range(i, j - 1):
                tmp = node.next
                node.next = node.next.next
                tmp.next = pre.next
                pre.next = tmp
            pre, node = node, node.next
            i = j
        return dummy.next

    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        dq = deque()
        pre, node = dummy, head
        while node:
            dq.append(node)
            tmp = node.next
            if len(dq) == k:
                while dq:
                    pre.next = dq.pop()
                    pre = pre.next
                pre.next = None
            node = tmp
        while dq:
            pre.next = dq.popleft()
            pre = pre.next
        return dummy.next

    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = tail = dummy
        while True:
            count = k
            while count and tail:
                tail = tail.next
                count -= 1
            if not tail: break
            head = pre.next
            while pre.next != tail:
                tmp = pre.next
                pre.next = pre.next.next
                tmp.next = tail.next
                tail.next = tmp
            pre = tail = head
        return dummy.next

    def reverseKGroup3(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while count != k and cur:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    node = head
    for i in range(2, 6):
        node.next = ListNode(i)
        node = node.next
    print(s.reverseKGroup1(head, 5))
