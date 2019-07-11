# @Time    : 2019/7/10 20:42
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """bfs"""
        q1 = [node]
        ans = Node(node.val, [])
        q2 = [ans]
        visited = set()
        while q1:
            cur1 = q1.pop()
            cur2 = q2.pop()
            visited.add(cur1)
            for neighbor in cur1.neighbors:
                if neighbor in visited: continue
                if neighbor not in q1:
                    q1.append(neighbor)
                    new_neighbor = Node(neighbor.val, [cur2])
                    cur2.neighbors.append(new_neighbor)
                    q2.append(new_neighbor)
                else:
                    for n in q2:
                        if n.val == neighbor.val:
                            cur2.neighbors.append(n)
                            n.neighbors.append(cur2)
                            break
        return ans

    def cloneGraph1(self, node: 'Node') -> 'Node':
        """dfs"""
        memo = {}

        def dfs(node: 'Node') -> 'Node':
            if node.val in memo: return memo[node.val]
            new_node = Node(node.val, [])
            memo[node.val] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node

        return dfs(node)

    def cloneGraph2(self, node: 'Node') -> 'Node':
        """非递归 dfs"""
        stack = [node]
        memo = {}
        memo[node.val] = Node(node.val, [])
        while stack:
            cur = stack.pop()
            for neighbor in cur.neighbors:
                if neighbor.val not in memo:
                    stack.append(neighbor)
                    memo[neighbor.val] = Node(neighbor.val, [])
                memo[cur.val].neighbors.append(memo[neighbor.val])
        return memo[node.val]

    def cloneGraph3(self, node: 'Node') -> 'Node':
        """bfs"""
        q = deque([node])
        memo = {}
        memo[node.val] = Node(node.val, [])
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor.val not in memo:
                    q.append(neighbor)
                    memo[neighbor.val] = Node(neighbor.val, [])
                memo[cur.val].neighbors.append(memo[neighbor.val])
        return memo[node.val]
