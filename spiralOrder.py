# @Time    : 2019/6/2 10:06
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        is_row, res = True, []
        r, c = len(matrix), len(matrix[0])
        visited = set()
        i = j = 0
        inc = 0
        while len(visited) < r * c:
            visited.add((i, j))
            res.append(matrix[i][j])
            if is_row and 0 <= j < c:
                if inc == 0:
                    if (i, j + 1) in visited or j + 1 >= c:
                        is_row = False
                        inc = 1
                        i += 1
                    else:
                        j += 1
                elif inc == 2:
                    if (i, j - 1) in visited or j - 1 < 0:
                        is_row = False
                        inc = 3
                        i -= 1
                    else:
                        j -= 1
            elif not is_row and 0 <= i < r:
                if inc == 1:
                    if (i + 1, j) in visited or i + 1 >= r:
                        is_row = True
                        inc = 2
                        j -= 1
                    else:
                        i += 1
                elif inc == 3:
                    if (i - 1, j) in visited or i - 1 < 0:
                        is_row = True
                        inc = 0
                        j += 1
                    else:
                        i -= 1
        return res

    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        res, i, j, di, dj = [], 0, 0, 0, 1
        for _ in range(len(matrix) * len(matrix[0])):
            res.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == None:
                di, dj = dj, -di
            i += di
            j += dj
        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(s.spiralOrder(matrix))
    print(s.spiralOrder1(matrix))
