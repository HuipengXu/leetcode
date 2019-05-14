# @Time    : 2019/5/14 7:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Tuple, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ret = ListNode(0)

        def argmin(lists: List[ListNode]) -> Tuple[int, int]:
            idx = 0
            min_ = float('inf')
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_:
                    min_ = lists[i].val
                    idx = i
            return idx, min_

        node = ret
        while any(lists):
            idx, min_val = argmin(lists)
            node.next = ListNode(min_val)
            node = node.next
            lists[idx] = lists[idx].next
        return ret.next

    # 小顶堆
    def mergeKLists1(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not lists: return None
        ret = ListNode(0)
        heap = []
        # 建堆
        for i, lst in enumerate(lists):
            if lst: heapq.heappush(heap, (lst.val, i, lst))
        node = ret
        while heap:
            min_val, i, n = heapq.heappop(heap)
            node.next = n
            node = node.next
            if n.next:
                heapq.heappush(heap, (n.next.val, i, n.next))
            n.next = None
        return ret.next

    # 小顶堆，原地
    def mergeKLists2(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not lists: return None
        ret = ListNode(0)
        heap = []
        # 建堆
        for i, lst in enumerate(lists):
            val = lst.val if lst else float('inf')
            heapq.heappush(heap, (val, i))
            if lists[i]: lists[i] = lists[i].next
        node = ret
        while True:
            min_val, idx = heapq.heappop()
            if min_val == float('inf'): break
            node.next = ListNode(min_val)
            node = node.next
            new_val = lists[idx].val if lists[idx] else float('inf')
            heapq.heappush(heap, (new_val, idx))
            if lists[idx]: lists[idx] = lists[idx].next
        return ret.next

    # 分治
    def mergeKLists3(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not lists: return None

        def merge(n1: ListNode, n2: ListNode) -> ListNode:
            if not n1 and n2: return n2
            if not n2 and n1: return n1
            ret = ListNode(0)
            node = ret
            while n1 and n2:
                if n1.val < n2.val:
                    node.next = ListNode(n1.val)
                    n1 = n1.next
                else:
                    node.next = ListNode(n2.val)
                    n2 = n2.next
                node = node.next
            if n1: node.next = n1
            if n2: node.next = n2
            return ret.next

        def merge_part_c(start: int, end: int) -> ListNode:
            if end - start <= 1: return lists[start]
            mid = start + ((end - start) >> 1)
            n1 = merge_part_c(start, mid)
            n2 = merge_part_c(mid, end)
            n = merge(n1, n2)
            return n

        return merge_part_c(0, len(lists))

    # 分治，原地
    def mergeKLists4(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not lists: return None

        def merge(n1: ListNode, n2: ListNode) -> ListNode:
            if not n1 and n2: return n2
            if not n2 and n1: return n1
            ret = ListNode(0)
            node = ret
            while n1 and n2:
                if n1.val < n2.val:
                    node.next = n1
                    n1 = n1.next
                else:
                    node.next = n2
                    n2 = n2.next
                node = node.next
            if n1: node.next = n1
            if n2: node.next = n2
            return ret.next

        def merge_part_c(start: int, end: int) -> ListNode:
            if end - start <= 1: return lists[start]
            mid = start + ((end - start) >> 1)
            n1 = merge_part_c(start, mid)
            n2 = merge_part_c(mid, end)
            n = merge(n1, n2)
            return n

        return merge_part_c(0, len(lists))

    # 分治，原地
    def mergeKLists5(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not lists: return None

        def merge(n1: ListNode, n2: ListNode) -> ListNode:
            if not n1: return n2
            if not n2: return n1
            if n1.val < n2.val:
                n1.next = merge(n1.next, n2)
                return n1
            else:
                n2.next = merge(n1, n2.next)
                return n2

        def merge_part_c(start: int, end: int) -> ListNode:
            if end - start <= 1: return lists[start]
            mid = start + ((end - start) >> 1)
            n1 = merge_part_c(start, mid)
            n2 = merge_part_c(mid, end)
            n = merge(n1, n2)
            return n

        return merge_part_c(0, len(lists))
