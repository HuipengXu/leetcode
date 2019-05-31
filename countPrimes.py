# @Time    : 2019/5/31 11:57
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        for i in range(2, n):
            flag = True
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    flag = False
                    break
            if flag: cnt += 1
        return cnt

    # 厄拉多塞筛法
    def countPrimes1(self, n: int) -> int:
        if n < 2: return 0
        visited = {1}
        for i in range(2, int(sqrt(n)) + 1):
            if i in visited: continue
            j = 2
            while j * i < n:
                visited.add(j * i)
                j += 1
        return n - len(visited) - 1


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes1(10))
