# @Time    : 2019/5/17 14:20
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # 超出时间限制
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        n = len(heights)
        left = [i for i in range(n)]
        right = [i for i in range(1, n + 1)]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if heights[j] >= heights[i]:
                    left[i] -= 1
                else:
                    break
            for k in range(i + 1, n):
                if heights[k] >= heights[i]:
                    right[i] += 1
                else:
                    break
        max_area = 0
        for m in range(n):
            max_area = max(max_area, (right[m] - left[m]) * heights[m])
        return max_area

    # 超时
    def largestRectangleArea1(self, heights: List[int]) -> int:
        if not heights: return 0
        max_area = heights[0]
        for i in range(1, len(heights) + 1):
            if i < len(heights) and heights[i] >= heights[i - 1]:
                continue
            j = i - 1
            while j >= 0:
                max_area = max(max_area, min(heights[j:i]) * (i - j))
                j -= 1
        return max_area

    # 丑的不能看
    def largestRectangleArea2(self, heights: List[int]) -> int:
        if not heights: return 0
        stack = [0]
        max_area = heights[0]
        for i in range(1, len(heights)):
            right = i
            if heights[i] >= heights[stack[-1]]:
                if i == len(heights) - 1:
                    right = len(heights)
                    max_area = max(max_area, (right - stack[-1] - 1) * heights[-1])
                else:
                    stack.append(i)
                    continue
            flag = True
            while stack and (heights[stack[-1]] > heights[i] or i == len(heights) - 1):
                if i == len(heights) - 1 and heights[stack[-1]] < heights[i] and flag:
                    right = len(heights)
                    flag = False
                    stack.append(i)
                cur = stack.pop()
                while stack and heights[stack[-1]] == heights[cur]:
                    stack.pop()
                left = stack[-1] if stack else -1
                max_area = max(max_area, (right - left - 1) * heights[cur])
            stack.append(i)
        return max_area

    def largestRectangleArea3(self, heights: List[int]) -> int:
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


if __name__ == '__main__':
    heights = [5, 5, 1, 7, 1, 1, 5, 2, 7, 8]
    s = Solution()
    print(s.largestRectangleArea(heights))
    print(s.largestRectangleArea1(heights))
    print(s.largestRectangleArea2(heights))
    print(s.largestRectangleArea3(heights))
