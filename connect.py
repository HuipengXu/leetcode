# @Time    : 2019/6/6 9:15
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(root: Node) -> None:
            if not root or not root.left: return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            helper(root.left)
            helper(root.right)

        helper(root)
        return root

    def connect1(self, root: 'Node') -> Optional['Node']:
        if not root: return
        first = node = root
        while first:
            next_ = first.next
            while node.left:
                node.left.next = node.right
                if next_:
                    node.right.next = next_.left
                    node, next_ = next_, next_.next
                else:
                    break
            first = node = first.left
        return root
