# @Time    : 2019/6/11 14:59
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def back_tracking(i: int, tmp: List[str]) -> None:
            if i == n:
                res.append(tmp)
                return
            for j in range(n):
                if valid(i, j, tmp) or i == 0:
                    back_tracking(i + 1, tmp + ['.' * j + 'Q' + '.' * (n - j - 1)])

        def valid(i: int, j: int, cur: List[str]) -> bool:
            for k in range(i - 1, -1, -1):
                if cur[k][j] == 'Q':
                    return False
                if j - (i - k) >= 0 and cur[k][j - (i - k)] == 'Q':
                    return False
                if j + (i - k) < n and cur[k][j + (i - k)] == 'Q':
                    return False
            return True

        back_tracking(0, [])
        return res

    def solveNQueens1(self, n: int) -> List[List[str]]:
        res = []

        def dfs(queens: List[int], xy_diff: List[int], xy_sum: List[int]) -> None:
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and (p - q) not in xy_diff and (p + q) not in xy_sum:
                    dfs(queens + [q], xy_diff + [p - q], xy_sum + [p + q])

        dfs([], [], [])
        return [['.' * q + 'Q' + '.' * (n - q - 1) for q in queens] for queens in res]


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
    print(s.solveNQueens1(4))
