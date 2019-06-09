# @Time    : 2019/6/10 6:56
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []

        def recur(root: TreeNode, level: int):
            if not root: return
            if len(levels) == level:
                levels.append([])
            levels[level].append(root.val)
            recur(root.left, level + 1)
            recur(root.right, level + 1)

        recur(root, 0)
        return levels[::-1]

    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        dq = deque([root])
        levels = []
        while dq:
            tmp = []
            length = len(dq)
            for _ in range(length):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            levels.append(tmp)
        return levels[::-1]

    def levelOrderBottom2(self, root):
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue if node for child in (node.left, node.right)]
        return res[-2::-1]
