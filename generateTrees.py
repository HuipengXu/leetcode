# @Time    : 2019/6/15 7:56
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(first: int, last: int) -> List[TreeNode]:
            res = []
            for val in range(first, last):
                for l_tree in dfs(first, val):
                    for r_tree in dfs(val + 1, last):
                        root = TreeNode(val)
                        root.left, root.right = l_tree, r_tree
                        res += root
            return res or [None]

        return dfs(1, n + 1)

    def generateTrees1(self, n: int) -> List[TreeNode]:
        def generate(first, last):
            trees = []
            for root in range(first, last + 1):
                for left in generate(first, root - 1):
                    for right in generate(root + 1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        # 秀，逗号形成列表
                        trees += node,
            return trees or [None]

        return generate(1, n)


if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees1(3))
