# @Time    : 2019/6/3 9:05
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for num in range(1, n ** 2 + 1):
            res[i][j] = num
            if res[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
