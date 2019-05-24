# @Time    : 2019/5/24 13:27
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B: return 0
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        max_len = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(dp[i][j], max_len)
        return max_len

    def findLength1(self, A: List[int], B: List[int]) -> int:
        if not A or not B: return 0
        dp = [0] * (len(B) + 1)
        max_len = 0
        for i in range(1, len(A) + 1):
            upper_left = dp[0]
            for j in range(1, len(B) + 1):
                tmp = dp[j]
                if A[i - 1] == B[j - 1]:
                    dp[j] = upper_left + 1
                    max_len = max(dp[j], max_len)
                else:
                    dp[j] = 0
                upper_left = tmp
        return max_len


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 4, 4, 2, 62, 1]
    B = [3, 2, 1, 4, 4, 7, 4, 1, 6, 4, 3]
    print(s.findLength(A, B))
    print(s.findLength1(A, B))
