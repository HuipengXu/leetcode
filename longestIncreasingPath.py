# @Time    : 2019/4/25 21:09
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import defaultdict


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        if row == 0: return 0
        col = len(matrix[0])
        ret = 1
        length_map = defaultdict(int)

        def bt(i: int, j: int, length: int):
            nonlocal ret
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            if length_map[(i, j)] >= length: return
            ret = max(ret, length)
            length_map[(i, j)] = length
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                bt(i - 1, j, length + 1)
            if i + 1 < row and matrix[i + 1][j] > matrix[i][j]:
                bt(i + 1, j, length + 1)
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                bt(i, j - 1, length + 1)
            if j + 1 < col and matrix[i][j + 1] > matrix[i][j]:
                bt(i, j + 1, length + 1)

        for i in range(row):
            for j in range(col):
                bt(i, j, 1)
        return ret if col else 0

    # 通过
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        row = len(matrix)
        col = len(matrix[0])
        length_map = defaultdict(int)

        def dfs(i: int, j: int):
            if (i, j) in length_map: return length_map[(i, j)]
            tmp = 1
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                tmp = max(tmp, dfs(i - 1, j) + 1)
            if i + 1 < row and matrix[i + 1][j] > matrix[i][j]:
                tmp = max(tmp, dfs(i + 1, j) + 1)
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                tmp = max(tmp, dfs(i, j - 1) + 1)
            if j + 1 < col and matrix[i][j + 1] > matrix[i][j]:
                tmp = max(tmp, dfs(i, j + 1) + 1)
            length_map[(i, j)] = tmp
            return tmp

        ret = 1
        for i in range(row):
            for j in range(col):
                ret = max(ret, dfs(i, j))
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    print(s.longestIncreasingPath(nums))
    print(s.longestIncreasingPath1(nums))
