# @Time    : 2019/6/10 10:41
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root: return res

        def dfs(root: TreeNode, tmp: list, sum: int) -> None:
            if not root.left and not root.right:
                if root.val == sum:
                    res.append(tmp + [root.val])
            if root.left:
                dfs(root.left, tmp + [root.val], sum - root.val)
            if root.right:
                dfs(root.right, tmp + [root.val], sum - root.val)

        dfs(root, [], sum)
        return res
