# @Time    : 2019/4/19 10:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf') if root is not None else 0

        def recur(node: TreeNode) -> int:
            nonlocal max_sum
            if node is None: return 0
            left = recur(node.left)
            right = recur(node.right)
            sum_ = left + node.val + right
            left_sum = left + node.val
            right_sum = right + node.val
            ret = max(left_sum, right_sum, node.val)
            max_sum = max(max_sum, sum_, ret)
            return ret

        recur(root)
        return max_sum
