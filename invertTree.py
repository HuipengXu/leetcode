# @Time    : 2019/5/31 16:04
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def reverse(root: TreeNode) -> None:
            if not root: return
            reverse(root.left)
            reverse(root.right)
            root.left, root.right = root.right, root.left

        reverse(root)
        return root

    def invertTree1(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
