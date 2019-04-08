# @Time    : 2019/4/8 14:06
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> Optional['Node']:
        if head is None: return None
        nodes = {}
        node = head
        while node:
            nodes[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            nodes[node].next = nodes.get(node.next)
            nodes[node].random = nodes.get(node.random)
            node = node.next
        return nodes[head]
