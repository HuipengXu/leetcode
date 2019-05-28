# @Time    : 2019/5/28 7:57
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        nodes = deque([root])
        tmp = deque()
        while nodes:
            node = nodes.popleft()
            if node:
                tmp.append(node.left)
                tmp.append(node.right)
            if not nodes:
                low, high = 0, len(tmp) - 1
                while low < high:
                    if (tmp[low] is None and tmp[high] is None or
                            (tmp[low] is not None and tmp[high] is not None and
                             tmp[low].val == tmp[high].val)):
                        low += 1
                        high -= 1
                    else:
                        return False
                nodes = tmp
                tmp = deque()
        return True

    def isSymmetric1(self, root: TreeNode) -> bool:
        def is_mirror(root1: TreeNode, root2: TreeNode) -> bool:
            if root1 == root2 == None: return True
            if root1 == None or root2 == None: return False
            if root1 == root2:
                return is_mirror(root1.left, root2.right)
            else:
                return (root1.val == root2.val and is_mirror(root1.left, root2.right) and is_mirror(root1.right,
                                                                                                    root2.left))

        return is_mirror(root, root)

    def isSymmetric2(self, root: TreeNode) -> bool:
        dq = deque([root, root])
        while dq:
            r1 = dq.popleft()
            r2 = dq.popleft()
            if r1 == r2 == None: return True
            if r1 == None or r2 == None: return False
            if r1.val != r2.val: return False
            dq.append(r1.left)
            dq.append(r2.right)
            dq.append(r1.right)
            dq.append(r2.left)
        return True


if __name__ == '__main__':
    head = TreeNode(9)
    head.left = TreeNode(-42)
    head.right = TreeNode(-42)
    node = head.left
    node.right = TreeNode(76)
    node1 = head.right
    node1.left = TreeNode(76)
    node2 = node.right
    node3 = node1.left
    # node2.left = TreeNode(26)
    # node2.right = TreeNode(-61)
    node3.left = TreeNode(13)
    node3.left.left = TreeNode(13)
    s = Solution()
    print(s.isSymmetric(head))
