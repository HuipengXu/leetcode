# @Time    : 2019/6/6 13:53
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # 使用了额外空间
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        previous = [0] * len(board[0])
        surround = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                    (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(len(board)):
            left, tmp_previous = 0, board[i].copy()
            for j in range(len(board[0])):
                sum_, tmp = 0, board[i][j]
                for dx, dy in surround:
                    if dx == -1:
                        if 0 <= j + dy < len(board[0]):
                            tmp1 = previous[j + dy]
                        else:
                            tmp1 = 0
                        sum_ += tmp1
                    elif dx == 0 and dy == -1:
                        sum_ += left
                        left = tmp
                    else:
                        if i + dx < len(board) and 0 <= j + dy < len(board[0]):
                            tmp2 = board[i + dx][j + dy]
                        else:
                            tmp2 = 0
                        sum_ += tmp2
                if board[i][j] and (sum_ > 3 or sum_ < 2):
                    board[i][j] = 0
                elif board[i][j] == 0 and sum_ == 3:
                    board[i][j] = 1
            previous = tmp_previous

    def gameOfLife1(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return

        def g(i: int, j: int) -> int:
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                return board[i][j] & 1
            return 0

        surround = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                    (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                sum_ = 0
                for dx, dy in surround:
                    sum_ += g(i + dx, j + dy)
                if board[i][j]:
                    if sum_ < 2 or sum_ > 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3
                elif sum_ == 3:
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1


if __name__ == '__main__':
    s = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print(s.gameOfLife1(board))
    print(board)
