# @Time    : 2019/6/9 9:25
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 0

        def back_tracking(m: int, n: int) -> None:
            nonlocal res
            if len(s) - m < len(t) - n: return
            if n == len(t):
                res += 1
                return
            for i in range(m, len(s)):
                if s[i] == t[n]:
                    back_tracking(i + 1, n + 1)

        back_tracking(0, 0)
        return res

    def numDistinct1(self, s: str, t: str) -> int:
        dp = [1] * (len(s) + 1)
        for i in range(len(t)):
            left_upper, dp[0] = dp[0], 0
            for j in range(len(s)):
                tmp = dp[j + 1]
                if t[i] == s[j]:
                    dp[j + 1] = left_upper + dp[j]
                else:
                    dp[j + 1] = dp[j]
                left_upper = tmp
        return dp[-1]

    def numDistinct2(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for i in range(len(s)):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]

    def numDistinct3(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        map_ = [-1] * 128
        nexts = [0] * len(t)
        for i, c in enumerate(t):
            nexts[i] = map_[ord(c)]
            map_[ord(c)] = i
        for i in range(len(s)):
            j = map_[ord(s[i])]
            while j >= 0:
                dp[j + 1] += dp[j]
                j = nexts[j]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    ss = "rabbbit"
    t = "rabbit"
    print(s.numDistinct(ss, t))
    print(s.numDistinct1(ss, t))
    print(s.numDistinct2(ss, t))
    print(s.numDistinct3(ss, t))
