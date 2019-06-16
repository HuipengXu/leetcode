# @Time    : 2019/6/16 8:32
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        res = []
        stack = [root]

        while stack:
            if not stack[-1].left and not stack[-1].right:
                cur = stack.pop()
                res.append(cur.val)
                if not stack:
                    break
            last = stack[-1]
            if last.right:
                stack.append(last.right)
                last.right = None
            if last.left:
                stack.append(last.left)
                last.left = None

        return res

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []

        def recur(root: TreeNode) -> None:
            if not root: return
            recur(root.left)
            recur(root.right)
            res.append(root.val)

        recur(root)
        return res

    # 参考：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-hou-xu-bian-li-dian-xing-die-dai-fa-by-/
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        last, node = None, root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            cur = stack[-1]
            if not cur.right or last == cur.right:
                stack.pop()
                res.append(cur.val)
                last, node = cur, None
            else:
                node = cur.right
        return res

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        """
        更为简洁的写法。这种解法的思想是先序遍历的变形，先序遍历是“根->左->右”，
        后序遍历是“左->右->根”，那么把先序遍历改成“根->右->左”，再逆序一下就是后序遍历。
        """
        if not root: return []

        res, stack = [], [root]

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return res[::-1]



if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution()
    print(s.postorderTraversal(root))
