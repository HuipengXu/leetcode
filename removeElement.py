# @Time    : 2019/6/4 9:24
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j
