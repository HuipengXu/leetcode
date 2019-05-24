# @Time    : 2019/5/24 19:13
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # 日常超时
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        max_area = 0
        for i in range(1, len(height)):
            for j in range(i):
                max_area = max(max_area, min(height[i], height[j]) * (i - j))
                if height[j] >= height[i]:
                    break
        return max_area

    def maxArea1(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(height))
