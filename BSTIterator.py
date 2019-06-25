# @Time    : 2019/6/25 16:21
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    """
    不符合空间复杂度
    """

    def __init__(self, root: TreeNode):
        self.vals = []
        self.index = 0

        def in_order(root: TreeNode) -> None:
            if root:
                in_order(root.left)
                self.vals.append(root.val)
                in_order(root.right)

        in_order(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            res = self.vals[self.index]
            self.index += 1
            return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.vals)


class BSTIterator1:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.stack:
            cur = self.stack.pop()
            tmp = cur.right
            while tmp:
                self.stack.append(tmp)
                tmp = tmp.left
            return cur.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
