# @Time    : 2019/6/10 8:22
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res = True

        def height(root: TreeNode) -> Optional[int]:
            nonlocal res
            if not root or not res: return 0
            left = height(root.left) + 1
            right = height(root.right) + 1
            if abs(left - right) > 1:
                res = False
                return 0
            return max(left, right)

        height(root)
        return res

    def isBalanced1(self, root: TreeNode) -> bool:
        if not root: return True

        def height(root: TreeNode) -> Optional[int]:
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1

        return self.isBalanced1(root.left) and self.isBalanced1(root.right) and abs(
            height(root.left) - height(root.right)) <= 1
