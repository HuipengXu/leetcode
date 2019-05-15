# @Time    : 2019/5/15 20:21
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        max_side, r, c = 0, len(matrix), len(matrix[0])
        dp = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '0': continue
                left = dp[i][j - 1] if j - 1 >= 0 else 0
                upper = dp[i - 1][j] if i - 1 >= 0 else 0
                left_upper = dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
                dp[i][j] = min(left, upper, left_upper) + 1
                max_side = max(dp[i][j], max_side)
        return max_side ** 2

    # 降低空间复杂度
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        max_side, r, c = 0, len(matrix), len(matrix[0])
        dp = [0] * c
        for i in range(r):
            prev = dp[0]
            dp[0] = int(matrix[i][0])
            max_side = max(dp[0], max_side)
            for j in range(1, c):
                if matrix[i][j] == '0':
                    dp[j] = 0
                else:
                    tmp = dp[j]
                    dp[j] = min(prev, dp[j - 1], dp[j]) + 1
                    prev = tmp
                    max_side = max(dp[j], max_side)
        return max_side ** 2


if __name__ == '__main__':
    s = Solution()
    matrix = [["1", "0", "1", "1", "1"], ["0", "1", "0", "1", "0"], ["1", "1", "0", "1", "1"],
              ["1", "1", "0", "1", "1"], ["0", "1", "1", "1", "1"]]
    print(s.maximalSquare(matrix))
    print(s.maximalSquare1(matrix))
