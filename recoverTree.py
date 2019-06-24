# @Time    : 2019/6/24 9:58
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = [TreeNode(-float('inf'))]

        def in_order(root: TreeNode) -> None:
            if not root: return
            in_order(root.left)
            nodes.append(root)
            in_order(root.right)

        in_order(root)
        nodes.append(TreeNode(float('inf')))
        swap_nodes = []
        for i in range(1, len(nodes) - 1):
            if nodes[i - 1].val < nodes[i].val > nodes[i + 1].val:
                swap_nodes.append(nodes[i])
            elif nodes[i - 1].val > nodes[i].val < nodes[i + 1].val:
                swap_nodes.append(nodes[i])
        n0, n1 = swap_nodes[0], swap_nodes[-1]
        n0.val, n1.val = n1.val, n0.val

    def recoverTree1(self, root: TreeNode) -> None:
        prev = p0 = p1 = None

        def in_order(root: TreeNode) -> None:
            nonlocal prev, p0, p1
            if not root: return
            in_order(root.left)
            if prev and prev.val > root.val:
                p1 = root
                if not p0:
                    p0 = prev
            prev = root
            in_order(root.right)

        in_order(root)
        p0.val, p1.val = p1.val, p0.val

    def recoverTree2(self, root: TreeNode) -> None:
        prev = p0 = p1 = None
        node = root
        while node:
            if not node.left:
                if prev and prev.val > node.val:
                    p1 = node
                    if not p0:
                        p0 = prev
                prev = node
                node = node.right
            else:
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                if pre.right == None:
                    pre.right = node
                    node = node.left
                else:
                    if prev and prev.val > node.val:
                        p1 = node
                        if not p0:
                            p0 = prev
                    prev = node
                    pre.right = None
                    node = node.right
        p0.val, p1.val = p1.val, p0.val
