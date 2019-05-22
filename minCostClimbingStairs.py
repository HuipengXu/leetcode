# @Time    : 2019/5/22 17:53
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [0] * len(cost)
        dp[:2] = cost[:2]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[-1]

    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        cost.append(0)
        prev_prev, prev = cost[0], cost[1]
        ans = min(prev_prev, prev)
        for i in range(2, len(cost)):
            ans = min(prev_prev, prev) + cost[i]
            prev_prev = prev
            prev = ans
        return ans


if __name__ == '__main__':
    s = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(s.minCostClimbingStairs(cost))
    print(s.minCostClimbingStairs1(cost))
