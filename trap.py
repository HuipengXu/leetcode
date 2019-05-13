# @Time    : 2019/5/13 16:24
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


# 参考题解：https://leetcode-cn.com/problems/trapping-rain-water/solution/zuo-you-liang-bian-de-zui-da-zhi-by-powcai/

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0], max_right[-1] = height[0], height[-1]
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i - 1])
        for j in range(n - 2, -1, -1):
            max_right[j] = max(height[j], max_right[j + 1])
        ret = 0
        for m in range(n):
            ret += min(max_left[m], max_right[m]) - height[m]
        return ret

    def trap1(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        max_left = height[0]
        max_right = height[n - 1]
        left, right = 0, n - 1
        ret = 0
        while left < right:
            if height[left] < height[right]:
                if max_left > height[left]:
                    ret += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if max_right > height[right]:
                    ret += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        return ret

    # 最不好想
    def trap2(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i - stack[-1] - 1)
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
    print(s.trap1(height))
    print(s.trap2(height))
