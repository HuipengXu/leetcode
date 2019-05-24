# @Time    : 2019/5/24 14:34
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


class Solution:
    def soupServings(self, N: int) -> float:
        if N >= 4800: return 1.0
        memo = {}

        def recur(a: int, b: int) -> float:
            if (a, b) in memo: return memo[(a, b)]
            if a <= 0 and b <= 0: return 0.5
            if a <= 0:
                return 1.0
            elif b <= 0:
                return .0
            else:
                ans = 0.25 * (recur(a - 100, b) + recur(a - 75, b - 25) + recur(a - 50, b - 50) + recur(a - 25, b - 75))
            memo[(a, b)] = ans
            return ans

        return recur(N, N)
