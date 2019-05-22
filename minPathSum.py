# @Time    : 2019/5/22 8:35
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        dp = [0] * len(grid[0])
        dp[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[i] = grid[0][i] + dp[i - 1]
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                left = dp[j - 1] if j - 1 >= 0 else float('inf')
                upper = dp[j]
                dp[j] = min(left, upper) + grid[i][j]
        return dp[-1]

    def minPathSum1(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        dp = [grid[0][0]]
        for i in range(1, len(grid[0])):
            dp.append(grid[0][i] + dp[i - 1])
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                left = dp[j - 1] if j - 1 >= 0 else float('inf')
                upper = dp[j]
                dp[j] = min(left, upper) + grid[i][j]
        return dp[-1]
