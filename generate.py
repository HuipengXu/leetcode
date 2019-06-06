# @Time    : 2019/6/6 11:04
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * (i + 1) for i in range(numRows)]
        for i in range(1, numRows):
            for j in range(len(res[i])):
                left_upper = res[i - 1][j - 1] if j - 1 >= 0 else 0
                right_upper = res[i - 1][j] if j < len(res[i - 1]) else 0
                res[i][j] = left_upper + right_upper
        return res

    def generate1(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            tmp = []
            for j in range(len(res[i - 1]) + 1):
                left_upper = res[i - 1][j - 1] if j - 1 >= 0 else 0
                right_upper = res[i - 1][j] if j < len(res[i - 1]) else 0
                tmp.append(left_upper + right_upper)
            res.append(tmp)
        return res
