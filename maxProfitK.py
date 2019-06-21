# @Time    : 2019/6/21 14:34
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfitInf(prices: List[int]) -> int:
            dp_0, dp_1 = .0, -float('inf')
            for p in prices:
                tmp = dp_0
                dp_0 = max(dp_0, dp_1 + p)
                dp_1 = max(dp_1, tmp - p)
            return int(dp_0)

        length = len(prices)
        if k > length // 2:
            return maxProfitInf(prices)
        dp = [[[.0, .0] for _ in range(k + 1)] for _ in range(length + 1)]
        for i in range(length + 1):
            dp[i][0][1] = -float('inf')
        for i in range(k + 1):
            dp[0][i][1] = -float('inf')
        for i in range(1, length + 1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
        return int(dp[-1][k][0])


if __name__ == '__main__':
    s = Solution()
    prices = [2, 4, 1]
    print(s.maxProfit(2, prices))
