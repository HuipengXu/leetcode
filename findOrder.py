# @Time    : 2019/5/30 9:42
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import deque, defaultdict


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_table = []
        visited = set()
        for i in range(numCourses):
            adj_table.append(Node(i))
        for course, dep in prerequisites:
            node = adj_table[course]
            while node.next:
                node = node.next
            node.next = Node(dep)
        res = []

        def search_dep() -> List[int]:
            dep_nodes = []
            for head in adj_table:
                if head.next is None and head.val not in visited:
                    dep_nodes.append(head.val)
                    visited.add(head.val)
            return dep_nodes

        def delete_dep(dep: set) -> bool:
            res = False
            if not dep: return res
            for head in adj_table:
                node = head
                while node:
                    if node.next and node.next.val in dep:
                        res = True
                        node.next = node.next.next
                    else:
                        node = node.next
            return res

        tmp = search_dep()
        if not tmp: return []
        res.extend(tmp)
        while len(res) < numCourses:
            flag = delete_dep(set(tmp))
            if not flag: return []
            tmp = search_dep()
            res.extend(tmp)
        return res

    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for i, j in prerequisites:
            adj[j].append(i)
            in_degree[i] += 1
        dq = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                dq.append(i)
        res = []
        while dq:
            cur = dq.popleft()
            res.append(cur)
            for vertex in adj[cur]:
                in_degree[vertex] -= 1
                if in_degree[vertex] == 0:
                    dq.append(vertex)
        return res if not any(in_degree) else []

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_table = []
        visited = set()
        for i in range(numCourses):
            adj_table.append(Node(i))
        for course, dep in prerequisites:
            node = adj_table[course]
            while node.next:
                node = node.next
            node.next = Node(dep)
        res = []
        have_cycle = False

        def dfs(head: Node, path: set):
            nonlocal have_cycle
            if have_cycle: return
            if not head: return
            if head.val in visited: return
            if head.val in path:
                have_cycle = True
                return
            node = adj_table[head.val].next
            while node and not have_cycle:
                dfs(node, path | {head.val})
                node = node.next
            res.append(head.val)
            visited.add(head.val)

        for i in range(numCourses):
            dfs(adj_table[i], set())
        return res if not have_cycle else []

    # https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments.
    def findOrder3(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        neigh = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        queue = deque(i for i in range(numCourses) if not dic[i])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for n in neigh[node]:
                dic[n].remove(node)
                if not dic[n]:
                    dic.pop(n)
                    queue.append(n)
        return res if len(res) == numCourses else []


if __name__ == '__main__':
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(s.findOrder(numCourses, prerequisites))
    print(s.findOrder3(numCourses, prerequisites))
