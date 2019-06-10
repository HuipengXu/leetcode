# @Time    : 2019/6/10 8:52
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif not root.left:
            return self.minDepth(root.left) + 1
        elif not root.right:
            return self.minDepth(root.right) + 1
