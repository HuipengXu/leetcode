# @Time    : 2019/6/10 9:29
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res = False
        if not root: return False

        def dfs(root: TreeNode, sum_: int) -> None:
            nonlocal res
            if res: return
            if root.left and root.right:
                dfs(root.left, sum_ + root.val)
                dfs(root.right, sum_ + root.val)
            elif root.left:
                dfs(root.left, sum_ + root.val)
            elif root.right:
                dfs(root.right, sum_ + root.val)
            else:
                if sum_ + root.val == sum:
                    res = True
                return

        dfs(root, 0)
        return res

    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum1(root.left, sum - root.val) or self.hasPathSum1(root.right, sum - root.val)

    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        res = False
        if not root: return False

        def dfs(root: TreeNode, sum_: int) -> None:
            nonlocal res
            if res: return
            if root.left:
                dfs(root.left, sum_ + root.val)
            if root.right:
                dfs(root.right, sum_ + root.val)
            if not root.left and not root.right:
                if root.val + sum_ == sum:
                    res = True
                return

        dfs(root, 0)
        return res
