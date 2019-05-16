# @Time    : 2019/5/16 21:00
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]: return 0
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                    continue
                if j - 1 >= 0: dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    print(s.uniquePathsWithObstacles(obstacleGrid))
