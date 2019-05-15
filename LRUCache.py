# @Time    : 2019/5/14 21:37
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional
from collections import OrderedDict


class ListNode:

    def __init__(self, key: Optional[int], val: Optional[int]):
        self.key = key
        self.val = val
        self.next = None


class LRUCache:
    """
    基于单链表实现，超出时间限制
    """

    def __init__(self, capacity: int):
        self.head = ListNode(None, None)
        self.capacity = capacity
        self.cnt = 0

    def get(self, key: int) -> int:
        node = self.head.next
        prev = self.head
        while node:
            if node.key == key:
                break
            prev = node
            node = node.next
        if not node: return -1
        prev.next = node.next
        node.next = self.head.next
        self.head.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.head
        prev = None
        while node.next:
            if node.key == key:
                break
            prev = node
            node = node.next
        if node.key == key:
            node.val = value
            prev.next = node.next
            node.next = self.head.next
            self.head.next = node
            return
        self.cnt += 1
        new_node = ListNode(key, value)
        if self.cnt > self.capacity:
            prev.next = None
            self.cnt -= 1
        new_node.next = self.head.next
        self.head.next = new_node


class LRUCache1:
    """
    基于顺序哈希表，通过
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val != -1: self.cache.move_to_end(key, last=False)
        return val

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            self.cache.popitem()
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)


if __name__ == '__main__':
    lc = LRUCache1(2)
    lc.put(2, 1)
    lc.put(1, 1)
    lc.put(2, 3)
    lc.put(4, 1)
    print(lc.get(1))
    print(lc.get(2))
