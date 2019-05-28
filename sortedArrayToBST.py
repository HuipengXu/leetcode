# @Time    : 2019/5/28 10:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recur(nums: List[int]) -> Optional[TreeNode]:
            if not nums: return None
            root = TreeNode(nums[len(nums) // 2])
            root.left = recur(nums[:len(nums) // 2])
            root.right = recur(nums[len(nums) // 2 + 1:])
            return root

        return recur(nums)
