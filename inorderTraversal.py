# @Time    : 2019/5/29 8:53
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def in_order(root: TreeNode) -> None:
            if not root: return
            in_order(root.left)
            res.append(root.val)
            in_order(root.right)

        in_order(root)
        return res

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        stack = []
        res = []

        def helper(root: TreeNode):
            node = root
            while node:
                stack.append(node)
                node = node.left

        helper(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            helper(cur.right)
        return res
