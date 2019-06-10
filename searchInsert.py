# @Time    : 2019/6/10 16:16
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def searchInsert1(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    print(s.searchInsert(nums, 7))
    print(s.searchInsert(nums, 7))
