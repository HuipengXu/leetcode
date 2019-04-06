# @Time    : 2019/4/5 16:06
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Optional
import heapq


# 堆
def kthSmallest(matrix: List[List[int]], k: int) -> Optional[int]:
    if len(matrix[0]) == 0:
        return None
    elif len(matrix[0]) == 1:
        return matrix[0][0]
    heap = []
    for i in range(len(matrix)):
        heapq.heappush(heap, (matrix[0][i], 0, i))
    for j in range(k - 1):
        _, row, col = heapq.heappop(heap)
        if row + 1 >= len(matrix):
            continue
        heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
    return heapq.heappop(heap)[0]


# 二分
def super_kthSmallest(matrix: List[List[int]], k: int) -> Optional[int]:
    l = matrix[0][0]
    r = matrix[-1][-1]
    while l < r:
        m = l + ((r - l) >> 1)
        le_m = 0
        for row in matrix:
            for elem in row:
                if elem > m:
                    break
                le_m += 1
        if le_m >= k:
            r = m
        else:
            l = m + 1
    return l


if __name__ == "__main__":
    matrix = [[1, 6, 10],
              [6, 7, 12],
              [11, 14, 14]]
    k = 5
    print(kthSmallest(matrix, k))
    print(super_kthSmallest(matrix, k))
