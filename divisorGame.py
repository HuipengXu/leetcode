# @Time    : 2019/5/23 7:45
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N + 1)
        dp[0], dp[1] = True, False
        for i in range(1, N + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
        return dp[-1]

    def divisorGame1(self, N: int) -> bool:
        return (N & 1) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.divisorGame(6))
