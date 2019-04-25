# @Time    : 2019/4/24 19:40
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import defaultdict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if len(coins) == 0: return -1
        min_coin = min(coins)
        max_iter = amount // min_coin + 1
        dp = [0] * (amount + 1)
        cur = 0
        for c in coins:
            if c <= amount:
                dp[c] = 1
                cur = max(c, cur)
        it = 1
        while it < max_iter:
            if dp[amount] == 1: return it
            dp_tmp = [0] * (amount + 1)
            for c in coins:
                for i in range(cur, 0, -1):
                    if dp[i] == 0: continue
                    if i + c <= amount:
                        dp_tmp[i + c] = 1
                        cur = max(cur, i + c)
            it += 1
            dp = dp_tmp
        return -1

    # 比上面稍快一点，bfs
    def coinChange1(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = {0}
        visited = {0}
        it = 1
        while dp:
            dp_tmp = set()
            for a in dp:
                for c in coins:
                    if a + c == amount: return it
                    if a + c > amount:
                        break
                    if a + c in visited: continue
                    dp_tmp.add(a + c)
                    visited.add(a + c)
            dp = dp_tmp
            it += 1
        return -1

    # 我怎么这么傻，一开始便是从这个方向开始想，但是却一直卡在不知道什么情况才算无法找到组合；其实，通过动态规划有前面可达的所有状态
    # 推得后面的状态，只要到达金额 11 这个状态，如果没有组合那就是没有，从前到后已经考虑了所有的情况
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

    # dfs，tmd 又超时
    def coinChange3(self, coins: List[int], amount: int) -> int:
        amount_map = defaultdict(lambda: float('inf'))

        def bt(a: int, count: int):
            if a > amount:
                return
            if amount_map[a] <= count: return
            amount_map[a] = count
            for c in coins:
                bt(a + c, count + 1)

        bt(0, 0)
        ret = amount_map[amount] if amount_map[amount] < float('inf') else -1
        return ret if amount else 0

    # 来自：https://leetcode.com/problems/coin-change/discuss/77416/Python-11-line-280ms-DFS-with-early-termination-99-up
    def coinChange4(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        lenc, res = len(coins), 2 ** 31 - 1

        def dfs(pt, rem, count):
            nonlocal res
            if not rem:
                res = min(res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (res - count):  # if hope still exists
                    dfs(i, rem - coins[i], count + 1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return res if res < 2 ** 31 - 1 else -1

if __name__ == '__main__':
    coins = [470, 18, 66, 301, 403, 112, 360]
    amount = 8235
    s = Solution()
    print(s.coinChange1(coins, amount))
    print(s.coinChange2(coins, amount))
    print(s.coinChange3(coins, amount))
    print(s.coinChange4(coins, amount))
