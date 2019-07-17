# @Time    : 2019/7/17 15:58
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx_map = {}
        for i, num in enumerate(nums):
            if num in idx_map and i - idx_map[num] <= k:
                return True
            idx_map[num] = i
        return False
