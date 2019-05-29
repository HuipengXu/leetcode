# @Time    : 2019/5/29 7:53
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]: return False
        width, length = len(board), len(board[0])
        res = False

        def dfs(i: int, j: int, k: int, visited: Set[Tuple[int, int]]):
            nonlocal res
            if res: return
            if k == len(word):
                res = True
                return
            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if (0 <= x < width and 0 <= y < length and
                        (x, y) not in visited and word[k] == board[x][y]):
                    dfs(x, y, k + 1, visited | {(x, y)})

        for i in range(width):
            for j in range(length):
                if res: return res
                if board[i][j] != word[0]: continue
                dfs(i, j, 1, {(i, j)})
        return res
