# @Time    : 2019/6/23 13:38
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root: return res

        def dfs(root: TreeNode, tmp: List[str]) -> None:
            if not root.left and not root.right:
                res.append('->'.join(tmp + [str(root.val)]))
                return
            if root.left:
                dfs(root.left, tmp + [str(root.val)])
            if root.right:
                dfs(root.right, tmp + [str(root.val)])

        dfs(root, [])
        return res
