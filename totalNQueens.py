# @Time    : 2019/6/24 7:45
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Set, Tuple, List


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        def backtracking(i: int, tmp: Set[Tuple[int, int]]) -> None:
            nonlocal res
            if i == n:
                res += 1
                return
            for j in range(n):
                if valid(i, j, tmp):
                    backtracking(i + 1, tmp | {(i, j)})

        def valid(i: int, j: int, visited: Set[Tuple[int, int]]) -> bool:
            delta_col = 1
            for row in range(i - 1, -1, -1):
                if (row, j) in visited:
                    return False
                if j - delta_col >= 0 and (row, j - delta_col) in visited:
                    return False
                if j + delta_col < n and (row, j + delta_col) in visited:
                    return False
                delta_col += 1
            return True

        backtracking(0, set())
        return res

    def totalNQueens1(self, n: int) -> int:
        res = 0

        def backtracking(queens: Set[int], xy_diff: Set[int], xy_sum: Set[int]) -> None:
            nonlocal res
            p = len(queens)
            if p == n:
                res += 1
                return
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    backtracking(queens | {q}, xy_diff | {p - q}, xy_sum | {p + q})

        backtracking(set(), set(), set())
        return res

    def totalNQueens2(self, n):
        """
        :type n: int
        :rtype: int
        """

        def backtrack(row=0, hills=0, next_row=0, dales=0, count=0):
            """
            :type row: 当前放置皇后的行号
            :type hills: 主对角线占据情况 [1 = 被占据，0 = 未被占据]
            :type next_row: 下一行被占据的情况 [1 = 被占据，0 = 未被占据]
            :type dales: 次对角线占据情况 [1 = 被占据，0 = 未被占据]
            :rtype: 所有可行解的个数
            """
            if row == n:  # 如果已经放置了 n 个皇后
                count += 1  # 累加可行解
            else:
                # 当前行可用的列
                # ! 表示 0 和 1 的含义对于变量 hills, next_row and dales的含义是相反的
                # [1 = 未被占据，0 = 被占据]
                free_columns = columns & ~(hills | next_row | dales)

                # 找到可以放置下一个皇后的列
                while free_columns:
                    # free_columns 的第一个为 '1' 的位
                    # 在该列我们放置当前皇后
                    curr_column = - free_columns & free_columns

                    # 放置皇后
                    # 并且排除对应的列
                    free_columns ^= curr_column

                    count = backtrack(row + 1,
                                      (hills | curr_column) << 1,
                                      next_row | curr_column,
                                      (dales | curr_column) >> 1,
                                      count)
            return count

        # 棋盘所有的列都可放置，
        # 即，按位表示为 n 个 '1'
        # bin(cols) = 0b1111 (n = 4), bin(cols) = 0b111 (n = 3)
        # [1 = 可放置]
        columns = (1 << n) - 1
        return backtrack()


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens2(4))
