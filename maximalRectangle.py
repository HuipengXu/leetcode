# @Time    : 2019/5/17 10:09
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        max_rec = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_rec = max(max_rec, self.largestRectangleArea(heights))
        return max_rec

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        stack = []
        max_area = 0
        for i in range(len(heights)):
            right = i
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                continue
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                while stack and heights[stack[-1]] == heights[cur]:
                    stack.pop()
                left = stack[-1] if stack else -1
                max_area = max(max_area, (right - left - 1) * heights[cur])
            stack.append(i)
        right = len(heights)
        while stack:
            cur = stack.pop()
            while stack and heights[stack[-1]] == heights[cur]:
                stack.pop()
            left = stack[-1] if stack else -1
            max_area = max(max_area, (right - left - 1) * heights[cur])
        return max_area

    # 以后再看吧，不想看了。。。
    def maximalRectangle1(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        nums = [int(''.join(row), base=2) for row in matrix]
        ans, N = 0, len(nums)
        for i in range(N):
            j, num = i, nums[i]
            while j < N:
                num = num & nums[j]
                if not num:
                    break
                l, curnum = 0, num
                while curnum:
                    l += 1
                    curnum = curnum & (curnum << 1)
                ans = max(ans, l * (j - i + 1))
                j += 1
        return ans


if __name__ == '__main__':
    ss = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(ss.maximalRectangle(matrix))
    print(ss.maximalRectangle1(matrix))
