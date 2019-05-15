# @Time    : 2019/5/15 18:31
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_left = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_left:
                min_left = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_left)
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(prices))
