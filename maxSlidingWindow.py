# @Time    : 2019/4/6 17:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
import heapq


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    if k == 1: return nums
    ret = []
    for i in range(len(nums) - k + 1):
        ret.append(max(nums[i:i + k]))
    return ret


# 双端队列，时间复杂度 O(n)，每个元素各入队出队一次
def super_maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    if k == 1 or len(nums) == 0: return nums
    window, ret = [], []
    for idx, num in enumerate(nums):
        # 保证当前队首的最大元素在窗口的范围内
        if idx >= k and window[0] <= idx - k:
            window.pop(0)
        # 删去不可能成为最大值的元素
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(idx)
        if idx + 1 >= k:
            ret.append(nums[window[0]])
    return ret


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(maxSlidingWindow(nums, k))
    print(super_maxSlidingWindow(nums, k))
