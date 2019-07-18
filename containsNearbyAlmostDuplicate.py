# @Time    : 2019/7/18 15:53
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
import math


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        num_with_idx = [(num, i) for i, num in enumerate(nums)]
        num_with_idx.sort()
        for i in range(len(num_with_idx)):
            for j in range(i + 1, len(num_with_idx)):
                if num_with_idx[j][0] - num_with_idx[i][0] > t:
                    break
                if math.fabs(num_with_idx[j][1] - num_with_idx[i][1]) <= k:
                    return True
        return False

    def containsNearbyAlmostDuplicate1(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}

        for i, num in enumerate(nums):
            m = num // (t + 1)
            if m in buckets: return True
            if m - 1 in buckets and num - buckets[m - 1] <= t: return True
            if m + 1 in buckets and buckets[m + 1] - num <= t: return True
            buckets[m] = num
            if i >= k: buckets.pop(nums[i - k] // (t + 1))

        return False
