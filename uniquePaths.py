# @Time    : 2019/5/16 20:14
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0: return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths1(self, m: int, n: int) -> int:
        if m == 0 or n == 0: return 0
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if j - 1 >= 0:
                    dp[j] += dp[j - 1]
        return dp[-1]

    # 数学解法
    def uniquePaths2(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // math.factorial(m - 1) // math.factorial(n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(56, 90))
    print(s.uniquePaths1(56, 90))
    print(s.uniquePaths2(56, 90))
