# @Time    : 2019/6/5 10:02
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        last = -float('inf')

        def recur(root: TreeNode) -> bool:
            nonlocal last
            if not root: return True
            if recur(root.left):
                if root.val > last:
                    last = root.val
                    return recur(root.right)
            return False

        return recur(root)

    def isValidBST1(self, root: TreeNode) -> bool:
        def helper(root: TreeNode, lower: float, upper: float) -> bool:
            if not root: return True
            if lower < root.val < upper:
                return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)
            return False

        return helper(root, -float('inf'), float('inf'))
