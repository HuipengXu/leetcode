# @Time    : 2019/4/21 8:28
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


import math


class Solution:
    # 超时
    def numSquares0(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def recur(n: int):
            min_count = n
            base = 1
            while n - base ** 2 >= 0:
                if n - base ** 2 == 0:
                    memo[n] = 1
                    return 1
                count = recur(n - base ** 2) + 1
                min_count = min(min_count, count)
                base += 1
            memo[n] = min_count
            return min_count

        recur(n)
        return memo[n]

    # 超时
    def numSquares1(self, n: int) -> int:
        memo = [-1] * (n + 1)
        memo[0] = 0
        for i in range(1, n + 1):
            memo[i] = min(memo[i - j * j] for j in range(1, int(math.sqrt(i) + 1))) + 1
        return memo[n]

    # 四数平方和定理，通过
    def numSquares2(self, n: int) -> int:
        if n < 3: return n
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7: return 4
        i = 0
        while i * i <= n:
            j = int(math.sqrt(n - i ** 2))
            if i * i + j * j == n:
                return (not not i) + (not not j)
            i += 1
        return 3

    # 广度优先，通过
    def numSquares3(self, n: int) -> int:
        if n < 3: return n
        children = {n}
        ret = 0
        while children:
            ret += 1
            temp = set()
            for child in children:
                for base in range(1, int(math.sqrt(child) + 1)):
                    if child - base ** 2 == 0:
                        return ret
                    temp.add(child - base ** 2)
            children = temp
        return ret

    # 回溯
    def numSquares4(self, n: int) -> int:
        min_count = n

        def bt(n: int, count: int):
            nonlocal min_count
            if int(math.sqrt(n)) ** 2 == n:
                min_count = min(min_count, count + 1)
                return
            for i in range(1, int(math.sqrt(n) + 1)):
                bt(n - i ** 2, count + 1)

        bt(n, 0)
        return min_count


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares1(45))
    print(s.numSquares2(45))
    print(s.numSquares3(45))
    print(s.numSquares4(45))
