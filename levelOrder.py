# @Time    : 2019/6/3 12:02
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        res, layer = [], []
        dq = deque([root])
        tmp = deque()
        while dq:
            node = dq.popleft()
            layer.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if not dq:
                res.append(layer)
                dq = tmp
                tmp, layer = deque(), []
        return res

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root: return levels

        def helper(root: TreeNode, level: int):
            if len(levels) == level:
                levels.append([])
            levels[level].append(root.val)
            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)

        helper(root, 0)
        return levels

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root: return levels
        dq = deque([root])
        level = 0
        while dq:
            levels.append([])
            level_length = len(dq)
            for _ in range(level_length):
                node = dq.popleft()
                levels[level].append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
        return levels
