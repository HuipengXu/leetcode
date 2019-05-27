# @Time    : 2019/5/27 7:34
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [j for j in board[i] if j.isdigit()]
            if len(row) > len(set(row)): return False
        for item in zip(*board):
            col = [i for i in item if i.isdigit()]
            if len(col) > len(set(col)): return False
        for i in range(2, 9, 3):
            for j in range(2, 9, 3):
                sub = [board[m][n] for m in range(i - 2, i + 1) for n in range(j - 2, j + 1) if board[m][n].isdigit()]
                if len(sub) > len(set(sub)): return False
        return True

    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            tmp = set()
            for j in range(9):
                if board[i][j] is '.': continue
                if board[i][j] in col[j]: return False
                col[j].add(board[i][j])
                if board[i][j] in tmp: return False
                tmp.add(board[i][j])
                idx = (i // 3) * 3 + j // 3
                if board[i][j] in boxes[idx]: return False
                boxes[idx].add(board[i][j])
        return True
