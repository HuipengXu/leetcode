# @Time    : 2019/6/26 7:54
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1: return s
        col = math.ceil(len(s) / (2 * numRows - 2)) * (numRows - 1)
        res = [[''] * col for _ in range(numRows)]
        i = j = delta_j = 0
        delta_i = 1
        for letter in s:
            res[i][j] = letter
            if i == numRows - 1:
                delta_j = 1
                delta_i = -1
            elif i == 0:
                delta_i = 1
                delta_j = 0
            i += delta_i
            j += delta_j
        return ''.join(letter for row in res for letter in row if not letter.isspace())

    def convert1(self, s: str, numRows: int) -> str:
        if not s or numRows == 1: return s
        res = [''] * numRows
        i = 0
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    res[j] += s[i]
                    i += 1
            for j in range(numRows - 2, 0, -1):
                if i < len(s):
                    res[j] += s[i]
                    i += 1
        return ''.join(res)
