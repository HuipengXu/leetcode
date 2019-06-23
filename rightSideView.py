# @Time    : 2019/6/23 10:22
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        nodes = deque([root])
        while nodes:
            length = len(nodes)
            res.append(nodes[-1].val)
            for _ in range(length):
                cur = nodes.popleft()
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
        return res
