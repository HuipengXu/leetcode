# @Time    : 2019/6/22 13:36
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        dp = [i for i in range(-1, length)]
        for i in range(1, length):
            for j in range(i + 1):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)
        return dp[-1]


if __name__ == '__main__':
    ss = 'aaba'
    s = Solution()
    print(s.minCut(ss))
