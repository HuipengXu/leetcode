# @Time    : 2019/4/11 19:59
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest0(self, root: TreeNode, k: int) -> int:
        node_lists = []

        def recur(node):
            if node == None:
                return
            recur(node.left)
            if len(node_lists) == k:
                return
            node_lists.append(node)
            recur(node.right)

        recur(root)
        return node_lists[-1].val

    # 减少空间占用
    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        c, ret, flag = 0, None, True

        def recur(node):
            nonlocal c, ret, flag
            if node == None:
                return
            recur(node.left)
            if c < k: c += 1
            if c == k:
                if flag:
                    flag = False
                    ret = node
                return ret
            recur(node.right)

        recur(root)
        return ret.val

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        stack, c, node = [], 0, root
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            c += 1
            if c == k: return node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left
