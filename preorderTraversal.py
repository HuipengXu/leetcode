# @Time    : 2019/6/16 7:57
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        dq = [root]
        while dq:
            cur = dq.pop()
            if cur.right: dq.append(cur.right)
            if cur.left: dq.append(cur.left)
            res.append(cur.val)
        return res
