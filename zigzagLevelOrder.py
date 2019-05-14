# @Time    : 2019/5/14 20:43
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        children = []
        left = True
        nodes = deque([root])
        tmp = deque()
        while nodes:
            node = nodes.popleft()
            children.append(node.val)
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
            if not nodes:
                if left:
                    ret.append(children)
                else:
                    ret.append(children[::-1])
                left = False if left else True
                nodes = tmp
                tmp = deque()
                children = []
        return ret
