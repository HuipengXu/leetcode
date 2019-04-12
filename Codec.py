# @Time    : 2019/4/12 15:18
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None: return ""
        nodes, temp, ret, i = [root], [], [], 0
        while any(nodes):
            node = nodes[i]
            if node == None:
                ret.append(None)
            else:
                ret.append(node.val)
                temp.append(node.left)
                temp.append(node.right)
            i += 1
            if i == len(nodes):
                nodes = temp
                temp = []
                i = 0
        while ret[-1] == None:
            ret.pop()
        return str(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        elems = data[1:len(data) - 1]
        elem_lst = elems.split(', ')
        for m in range(len(elem_lst)):
            if elem_lst[m].isdigit() or elem_lst[m].startswith('-'):
                elem_lst[m] = TreeNode(int(elem_lst[m]))
            else:
                elem_lst[m] = None
        i, j, k = 0, 1, 3
        while j < len(elem_lst):
            child = j
            for e in range(i, j):
                if elem_lst[e] is None: continue
                if child >= len(elem_lst): break
                elem_lst[e].left = elem_lst[child]
                if child + 1 >= len(elem_lst): break
                elem_lst[e].right = elem_lst[child + 1]
                child += 2
            i, j, non_none = j, k, 0
            if j >= len(elem_lst): break
            for n in range(i, j):
                if elem_lst[n] is not None:
                    non_none += 1
            k = 2 * non_none + j
        return elem_lst[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# 来源于 leetcode
from collections import deque


class Codec1:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        resList = []
        if not root:
            return ''
        nodeQueue = deque()
        nodeQueue.append(root)
        while len(nodeQueue) > 0:
            node = nodeQueue.popleft()
            if node == None:
                resList.append('#')
            else:
                resList.append(str(node.val))
                nodeQueue.append(node.left)
                nodeQueue.append(node.right)
        return ' '.join(resList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        resList = data.split(' ')
        length = len(resList)
        if not length:
            return None
        root = TreeNode(resList[0])
        nodeQueue = deque()
        nodeQueue.append(root)
        i = 1
        while i < length:
            node = nodeQueue.popleft()
            if resList[i] == '#':
                node.left = None
            else:
                node.left = TreeNode(resList[i])
                nodeQueue.append(node.left)
            i += 1
            if resList[i] == '#':
                node.right = None
            else:
                node.right = TreeNode(resList[i])
                nodeQueue.append(node.right)
            i += 1
        return root


# 来源于 leetcode
class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())
        return doit()
