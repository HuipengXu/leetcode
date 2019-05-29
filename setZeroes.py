# @Time    : 2019/5/29 19:08
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Set, Tuple


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0 or (i, j) in visited: continue
                for k in range(len(matrix)):
                    if matrix[k][j] == 0: continue
                    matrix[k][j] = 0
                    visited.add((k, j))
                for m in range(len(matrix[0])):
                    if matrix[i][m] == 0: continue
                    matrix[i][m] = 0
                    visited.add((i, m))

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        is_col = False
        for i in range(row):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(1, col):
                matrix[0][i] = 0
        if is_col:
            for i in range(row):
                matrix[i][0] = 0


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    s.setZeroes(matrix)
    print(matrix)
