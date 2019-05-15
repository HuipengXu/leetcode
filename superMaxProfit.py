# @Time    : 2019/5/15 19:03
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # 贪心
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        left = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                max_profit += prices[i - 1] - left
                left = prices[i]
        max_profit += prices[-1] - left
        return max_profit


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 3, 4, 5]
    print(s.maxProfit(prices))
