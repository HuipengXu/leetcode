# @Time    : 2019/1/18 10:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    236. 二叉树的最近公共祖先
    """

    # 方法一：先获取两个节点的路径再比较
    def lowestCommonAncestor0(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_ancestors = q_ancestors = None
        traversed_node = set()
        node = root
        temp_ancestors = []
        # 确定 p、q 各自的祖先
        while True:
            temp_ancestors.insert(0, node)
            if node.val == p.val and not isinstance(p_ancestors, list):
                p_ancestors = temp_ancestors.copy()
            if node.val == q.val and not isinstance(q_ancestors, list):
                q_ancestors = temp_ancestors.copy()
            if isinstance(p_ancestors, list) and isinstance(q_ancestors, list):
                break
            if node.left and node.left not in traversed_node:
                node = node.left
            elif node.right and node.right not in traversed_node:
                node = node.right
            else:
                traversed_node.add(node)
                node = root
                temp_ancestors.clear()
        # 判断哪个节点更接近根节点，提高查找最近祖先的效率
        if p_ancestors[0].val > q_ancestors[0].val:
            higher_ancestors = q_ancestors
            lower_ancestors = p_ancestors
        else:
            higher_ancestors = p_ancestors
            lower_ancestors = q_ancestors
        lowest_ancestor = None
        flag = False
        # 查找最近公共祖先
        for p1 in higher_ancestors:
            for p2 in lower_ancestors:
                if p1.val == p2.val:
                    lowest_ancestor = p1
                    flag = True
                    break
            if flag:
                break
        return lowest_ancestor

    # 递归查找
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor1(root.left, p, q)
        right = self.lowestCommonAncestor1(root.right, p, q)
        if left is None:
            return right
        if right is None:
            return left
        return root

    # 时间复杂度过高，重复搜索浪费时间
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def in_tree(root: 'TreeNode', target: 'TreeNode') -> bool:
            stack = []
            while root:
                stack.append(root)
                root = root.left
            while stack:
                node = stack.pop()
                if node == target: return True
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            return False

        if root == p or root == q: return root
        while True:
            if (in_tree(root.left, p) and in_tree(root.right, q)) or \
                    (in_tree(root.right, p) and in_tree(root.left, q)):
                return root
            elif in_tree(root.left, p) and in_tree(root.left, q):
                root = root.left
                if root == p or root == q: return root
            elif in_tree(root.right, p) and in_tree(root.right, q):
                root = root.right
                if root == p or root == q: return root
