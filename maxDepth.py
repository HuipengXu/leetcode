# @Time    : 2019/5/28 13:38
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0

        def back_tracking(node: TreeNode, depth: int):
            nonlocal max_depth
            if not node:
                max_depth = max(max_depth, depth)
                return
            back_tracking(node.left, depth + 1)
            back_tracking(node.right, depth + 1)
            return

        back_tracking(root, 0)
        return max_depth

    def maxDepth1(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth1(root.left), self.maxDepth1(root.right))
