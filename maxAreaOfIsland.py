# @Time    : 2019/5/12 15:54
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # dfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        if len(grid) == 0 or len(grid[0]) == 0: return max_area
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] or grid[i][j] == 0: continue
                tmp_area = 0
                children = [(i, j), ]
                while children:
                    r, c = children.pop()
                    if visited[r][c]: continue
                    visited[r][c] = 1
                    tmp_area += 1
                    if r - 1 >= 0 and grid[r - 1][c] and visited[r - 1][c] == 0:
                        children.append((r - 1, c))
                    if r + 1 < len(grid) and grid[r + 1][c] and visited[r + 1][c] == 0:
                        children.append((r + 1, c))
                    if c - 1 >= 0 and grid[r][c - 1] and visited[r][c - 1] == 0:
                        children.append((r, c - 1))
                    if c + 1 < len(grid[0]) and grid[r][c + 1] and visited[r][c + 1] == 0:
                        children.append((r, c + 1))
                max_area = max(max_area, tmp_area)
        return max_area

    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        max_area = 0
        if len(grid) == 0 or len(grid[0]) == 0: return max_area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: continue
                tmp_area = 0
                children = [(i, j), ]
                while children:
                    r, c = children.pop()
                    if grid[r][c] == 0: continue
                    grid[r][c] = 0
                    tmp_area += 1
                    if r - 1 >= 0 and grid[r - 1][c]:
                        children.append((r - 1, c))
                    if r + 1 < len(grid) and grid[r + 1][c]:
                        children.append((r + 1, c))
                    if c - 1 >= 0 and grid[r][c - 1]:
                        children.append((r, c - 1))
                    if c + 1 < len(grid[0]) and grid[r][c + 1]:
                        children.append((r, c + 1))
                max_area = max(max_area, tmp_area)
        return max_area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    s = Solution()
    print(s.maxAreaOfIsland(grid))
    print(s.maxAreaOfIsland1(grid))
