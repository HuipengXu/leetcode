# @Time    : 2019/5/16 9:37
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Union


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> Union[int, float]:
        length = len(triangle)
        dp = [float('inf')] * (2 * length + 1)
        dp[len(dp) // 2] = triangle[0][0]
        for i in range(1, length):
            k = length - i
            for j in range(len(triangle[i])):
                dp[k] = min(dp[k - 1], dp[k + 1]) + triangle[i][j]
                k += 2
        return min(dp[1:-1:2])

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]: return 0
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


if __name__ == '__main__':
    s = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(s.minimumTotal(triangle))
    print(s.minimumTotal1(triangle))
