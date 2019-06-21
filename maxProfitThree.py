# @Time    : 2019/6/21 8:26
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(start: int, end: int) -> int:
            max_profit = 0
            if end <= start: return max_profit
            min_price = prices[start]
            for p in prices[start + 1:end]:
                max_profit = max(max_profit, p - min_price)
                min_price = min(min_price, p)
            return max_profit

        max_profit = 0
        for i in range(len(prices)):
            p1 = helper(0, i)
            p2 = helper(i, len(prices))
            max_profit = max(max_profit, p1 + p2)
        return max_profit

    def maxProfit1(self, prices: List[int]) -> int:
        if not prices: return 0

        min_price, max_price = prices[0], prices[-1]
        cur_max_profit = cur_neg_profit = 0
        profit, neg_profit = [], []
        length = len(prices)

        for i in range(length):
            cur_max_profit = max(cur_max_profit, prices[i] - min_price)
            profit.append(cur_max_profit)
            min_price = min(min_price, prices[i])
            cur_neg_profit = min(cur_neg_profit, prices[length - i - 1] - max_price)
            neg_profit.append(cur_neg_profit)
            max_price = max(max_price, prices[length - i - 1])

        max_profit = 0
        for i in range(length):
            left = profit[i]
            right = -neg_profit[length - i - 1]
            max_profit = max(max_profit, left + right)
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [[[.0, .0] for _ in range(3)] for _ in range(len(prices) + 1)]
        for i in range(3):
            dp[0][i][1] = -float('inf')
        for i in range(len(prices) + 1):
            dp[i][0][1] = -float('inf')
        for i in range(1, len(prices) + 1):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i - 1])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i - 1])
        return int(dp[len(prices)][2][0])

    def maxProfit3(self, prices: List[int]) -> int:
        dp_1_0 = dp_2_0 = 0
        dp_1_1 = dp_2_1 = -float('inf')
        for i in range(len(prices)):
            dp_2_0 = max(dp_2_0, dp_2_1 + prices[i])
            dp_2_1 = max(dp_2_1, dp_1_0 - prices[i])
            dp_1_0 = max(dp_1_0, dp_1_1 + prices[i])
            dp_1_1 = max(dp_1_1, -prices[i])
        return dp_2_0
