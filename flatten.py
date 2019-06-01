# @Time    : 2019/6/1 15:31
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
    # 使用了额外空间
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        nodes = []

        def pre_order(root: TreeNode):
            if not root: return
            nodes.append(root)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        nodes[-1].left = None
        nodes[-1].right = None

    def flatten1(self, root: TreeNode) -> None:
        def insert_to_right(root: TreeNode) -> Optional[TreeNode]:
            if not root: return
            insert_to_right(root.left)
            insert_to_right(root.right)
            tmp, root.right, root.left = root.right, root.left, None
            while root.right != None:
                root = root.right
            root.right = tmp

        insert_to_right(root)

    def flatten2(self, root: TreeNode) -> None:
        if not root: return
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                tmp = node.right
                node.right = node.left
                node.left = None
                while node.right:
                    node = node.right
                node.right = tmp
                root = tmp
