# @Time    : 2019/6/2 7:59
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res = True

        def recur(n: int, remainder: int):
            nonlocal res
            if not res: return
            if remainder or n == 0:
                res = False
                return
            if n == 1:
                return
            recur(n // 2, n % 2)

        recur(n, 0)
        return res

    def isPowerOfTwo1(self, n: int) -> bool:
        return n > 0 and n & n - 1 == 0
