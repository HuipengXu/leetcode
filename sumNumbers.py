# 129. 求根到叶子节点数字之和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Solution1:

    def rec(self, node, sum):
        if node == None:
            return 0
        if not node.left and not node.right:
            return sum * 10 + node.val
        return self.rec(node.left, sum * 10 + node.val) + self.rec(node.right, sum * 10 + node.val)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.rec(root, 0)

# 栈
class Solution:    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        s = 0
        single_trace = root.val
        stack = []
        stack.append(root)
        if root.left == None and root.right == None:
            return single_trace
        fl = 1
        fr = 1
        while len(stack):
            temp = stack[-1]
            # if temp == None:
            #     break
            if temp.left:
                stack.append(temp.left)
                single_trace = single_trace * 10 + temp.left.val
                temp.left = None
                fl = 0
                fr = 1
            elif temp.right:
                stack.append(temp.right)
                single_trace = single_trace * 10 + temp.right.val
                temp.right = None
                fl = 1
                fr = 0
            else:
                if not fl:
                    s += single_trace
                    single_trace //= 10
                    fl = 1
                elif not fr:
                    s += single_trace
                    single_trace //= 10
                    fr = 1
                else:
                    single_trace //= 10
                stack.pop()
                
        return s