# @Time    : 2019/7/19 8:43
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import math


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area = (C - A) * (D - B) + (G - E) * (H - F)
        if A >= G or B >= H or F >= D or E >= C:
            return area
        x_min = max(A, E)
        y_min = max(B, F)
        x_max = min(C, G)
        y_max = min(D, H)
        return area - (x_max - x_min) * (y_max - y_min)
