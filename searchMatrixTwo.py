# @Time    : 2019/6/20 18:13
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        col_low, col_high = 0, len(matrix) - 1
        target_row = -1
        while col_low <= col_high:
            col_mid = col_low + ((col_high - col_low) >> 1)
            if matrix[col_mid][0] == target: return True
            if (col_mid + 1 < len(matrix) and matrix[col_mid][0] < target < matrix[col_mid + 1][0]
                    or col_mid + 1 == len(matrix) and matrix[col_mid][0] < target):
                target_row = col_mid
                break
            elif matrix[col_mid][0] > target:
                col_high = col_mid - 1
            else:
                col_low = col_mid + 1
        if target_row == -1: return False
        row_low, row_high = 0, len(matrix[target_row]) - 1
        while row_low <= row_high:
            row_mid = row_low + ((row_high - row_low) >> 1)
            if matrix[target_row][row_mid] == target:
                return True
            elif matrix[target_row][row_mid] < target:
                row_low = row_mid + 1
            else:
                row_high = row_mid - 1
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur > target:
                i -= 1
            else:
                j += 1
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        low, high = 0, len(matrix) * len(matrix[0]) - 1
        row = len(matrix[0])
        while low <= high:
            mid = low + ((high - low) >> 1)
            i, j = divmod(mid, row)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


if __name__ == '__main__':
    matrix = [[1]]
    s = Solution()
    print(s.searchMatrix(matrix, 2))
