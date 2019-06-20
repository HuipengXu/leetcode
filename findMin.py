# @Time    : 2019/6/20 19:59
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[low] <= nums[mid]:
                if nums[mid] <= nums[high]:
                    return nums[low]
                low = mid + 1
            elif nums[low] >= nums[mid]:
                if nums[mid] >= nums[high]:
                    return nums[high]
                high = mid - 1

    def findMin1(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
