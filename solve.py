# @Time    : 2019/5/28 14:46
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        length, width = len(board[0]), len(board)

        def dfs(i: int, j: int) -> None:
            if board[i][j] == 'O':
                board[i][j] = 'D'
                for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < width and 0 <= y < length:
                        dfs(x, y)

        for i in range(width):
            dfs(i, 0)
            dfs(i, length - 1)
        for j in range(length):
            dfs(0, j)
            dfs(width - 1, j)
        for i in range(width):
            for j in range(length):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def solve1(self, board: List[List[str]]) -> None:
        if not board or not board[0]: return
        length, width = len(board[0]), len(board)

        def bfs(i: int, j: int) -> None:
            if board[i][j] != 'O': return
            dq = deque([(i, j)])
            while dq:
                m, n = dq.popleft()
                board[m][n] = 'D'
                for x, y in [(m + 1, n), (m - 1, n), (m, n - 1), (m, n + 1)]:
                    if 0 <= x < width and 0 <= y < length and board[x][y] == 'O':
                        dq.append((x, y))

        for i in range(length):
            bfs(0, i)
            bfs(width - 1, i)
        for j in range(width):
            bfs(j, 0)
            bfs(j, length - 1)
        for i in range(width):
            for j in range(length):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    s = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    print(s.solve1(board))
