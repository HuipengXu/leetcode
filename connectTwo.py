# @Time    : 2019/6/10 13:26
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        first = root

        def helper(node: Node) -> None:
            if len(stack) == 0:
                stack.append(node)
            else:
                cur = stack.pop()
                cur.next = node
                stack.append(node)

        while first:
            next_ = first
            stack = []
            while next_:
                if next_.left:
                    helper(next_.left)
                if next_.right:
                    helper(next_.right)
                next_ = next_.next
            while first and not first.left and not first.right:
                first = first.next
            if first and first.left:
                first = first.left
            elif first and first.right:
                first = first.right
        return root

    def connect1(self, root: 'Node') -> 'Node':
        first = root
        while first:
            while first and not first.left and not first.right:
                first = first.next
            if not first: break
            next_, cur = first, None
            while next_:
                if next_.left:
                    if cur:
                        cur.next = next_.left
                    cur = next_.left
                if next_.right:
                    if cur:
                        cur.next = next_.right
                    cur = next_.right
                next_ = next_.next
            first = first.left if first.left else first.right
        return root
