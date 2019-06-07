# @Time    : 2019/6/7 10:42
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        base = 3
        while n > 1:
            while n < base and base > 3: base //= 3
            n, remainder = divmod(n, base)
            if remainder: return False
            base **= 2
        return True

    def isPowerOfThree1(self, n: int) -> bool:
        res = True
        if n <= 0: return not res

        def recur(n: int, base: int) -> None:
            nonlocal res
            if not res or n == 1: return
            while n < base and base > 3: base //= 3
            n, remainder = divmod(n, base)
            if remainder:
                res = False
                return
            base **= 2
            recur(n, base)

        recur(n, 3)
        return res

    # 3的幂次质因子只有3，而整数范围内的3的幂次最大是1162261467
    def isPowerOfThree2(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree2(45))
