# @Time    : 2019/6/1 14:33
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 愚蠢的写法
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(t1: TreeNode, t2: TreeNode) -> Optional[TreeNode]:
            if not t1 and not t2: return
            if t1 and t2:
                val = t1.val + t2.val
                left1, left2 = t1.left, t2.left
                right1, right2 = t1.right, t2.right
            elif t1:
                val = t1.val
                left1, left2 = t1.left, None
                right1, right2 = t1.right, None
            else:
                val = t2.val
                left1, left2 = None, t2.left
                right1, right2 = None, t2.right
            node = TreeNode(val)
            node.left = merge(left1, left2)
            node.right = merge(right1, right2)
            return node

        return merge(t1, t2)

    def mergeTrees1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(t1: TreeNode, t2: TreeNode) -> Optional[TreeNode]:
            if t1 and t2:
                t1.val += t2.val
                t1.left = merge(t1.left, t2.left)
                t1.right = merge(t1.right, t2.right)
                return t1
            return t1 or t2

        return merge(t1, t2)
