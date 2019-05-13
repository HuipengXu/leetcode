# @Time    : 2019/5/13 9:32
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from queue import Queue


class Solution:
    # dfs
    def findCircleNum(self, M: List[List[int]]) -> int:
        cnt = 0
        if len(M) == 0 or len(M[0]) == 0: return cnt
        for i in range(len(M)):
            if M[i][i] == 0: continue
            children = [(i, i)]
            cnt += 1
            while children:
                r, c = children.pop()
                if M[r][c] == 0: continue
                M[r][c] = 0
                for k in range(len(M[c])):
                    if M[c][k]:
                        children.append((c, k))
        return cnt

    # dfs
    def findCircleNum1(self, M: List[List[int]]) -> int:
        cnt = 0
        if len(M) == 0 or len(M[0]) == 0: return cnt

        def dfs(r):
            for i in range(len(M)):
                if M[r][i]:
                    M[r][i] = 0
                    dfs(i)

        for i in range(len(M)):
            if M[i][i]:
                cnt += 1
                dfs(i)
        return cnt

    # dfs
    def findCircleNum2(self, M: List[List[int]]) -> int:
        cnt = 0
        visited = set()

        def dfs(r):
            for i in range(len(M)):
                if M[r][i] and i not in visited:
                    visited.add(i)
                    dfs(i)

        for i in range(len(M)):
            if i not in visited:
                cnt += 1
                dfs(i)
        return cnt

    # bfs
    def findCircleNum3(self, M: List[List[int]]) -> int:
        cnt = 0
        q = Queue()
        n = len(M)
        visited = set()
        for i in range(n):
            if i in visited: continue
            q.put(i)
            while not q.empty():
                i = q.get()
                visited.add(i)
                for j in range(n):
                    if M[i][j] and j not in visited:
                        q.put(j)
            cnt += 1
        return cnt

    # bfs
    def findCircleNum4(self, M: List[List[int]]) -> int:
        cnt = 0
        n = len(M)
        visited = set()
        for i in range(n):
            if i in visited: continue
            q = Queue()
            q.put(i)
            while not q.empty():
                i = q.get()
                visited.add(i)
                for j in range(n):
                    if M[i][j] and j not in visited:
                        q.put(j)
            cnt += 1
        return cnt

    # 并查集
    def findCircleNum5(self, M: List[List[int]]) -> int:
        def find(x: int) -> int:
            while x != f[x]: x = f[x]
            return x

        n = len(M)
        f = list(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j]: f[find(j)] = find(i)
        return sum(find(x) == x for x in range(n))


if __name__ == '__main__':
    s = Solution()
    nums = [[1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1]]
    # print(s.findCircleNum(nums))
    # print(s.findCircleNum1(nums))
    # print(s.findCircleNum2(nums))
    # print(s.findCircleNum3(nums))
    print(s.findCircleNum5(nums))
