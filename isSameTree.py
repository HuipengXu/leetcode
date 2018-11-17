# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 广度遍历
    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p != None and q != None:
            p_stack = [p]
            q_stack = [q]
            while p_stack:
                p = p_stack.pop(0)
                q = q_stack.pop(0)
                left_flag = right_flag = True
                if p.val != q.val:
                    return False
                if p.left != None and q.left != None:
                    p_stack.append(p.left)
                    q_stack.append(q.left)
                    left_flag = False
                if any([p.left, q.left]) and left_flag:
                       return False
                if p.right != None and q.right != None:
                    p_stack.append(p.right)
                    q_stack.append(q.right)
                    right_flag = False
                if any([p.right, q.right]) and right_flag:
                       return False
            return True
        else:
            return False
    # 递归
    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p != None and q != None:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right) 
        else:
            return False