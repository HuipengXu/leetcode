# @Time    : 2019/5/22 19:02
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def recur(n: int) -> int:
            if n == 0 or n == 1: return 1
            if n in memo: return memo[n]
            ans = 0
            for i in range(1, n + 1):
                ans += recur(i - 1) * recur(n - i)
            memo[n] = ans
            return ans

        return recur(n)

    def numTrees1(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3))
    print(s.numTrees1(3))
