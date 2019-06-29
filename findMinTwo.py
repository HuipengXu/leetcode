# @Time    : 2019/6/29 8:08
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            while low < high and nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2, 2, 2, 0, 1]))
