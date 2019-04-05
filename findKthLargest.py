# @Time    : 2019/4/4 21:58
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import random
from typing import Optional, List


class Solution:

    def quick_sort(self, nums: List[int], k: int) -> None:
        def quick_sort_c(nums: List[int], start: int, end: int) -> None:
            mid = partition(nums, start, end)
            if mid is None: return
            if len(nums) - k < mid:
                quick_sort_c(nums, start, mid)
            else:
                quick_sort_c(nums, mid + 1, end)

        def partition(nums: List[int], start: int, end: int) -> Optional[int]:
            if end - start <= 1:
                return
            pivot_idx = random.randint(start, end - 1)
            nums[end - 1], nums[pivot_idx] = nums[pivot_idx], nums[end - 1]
            j = start
            for i in range(start, end):
                if nums[i] <= nums[end - 1]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            return j - 1

        quick_sort_c(nums, 0, len(nums))

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums, k)
        return nums[len(nums) - k]

    def super_findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums: List[int], start: int, end: int) -> int:
            pivot_idx = random.randint(start, end - 1)
            nums[end - 1], nums[pivot_idx] = nums[pivot_idx], nums[end - 1]
            j = start
            for i in range(start, end):
                if nums[i] >= nums[end - 1]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            return j - 1

        start, end = 0, len(nums)
        while True:
            mid = partition(nums, start, end)
            if k - 1 == mid:
                return nums[mid]
            elif k - 1 < mid:
                start = start
                end = mid
            else:
                start = mid + 1
                end = end



if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 4
    s = Solution()
    print(sorted(nums))
    print(s.super_findKthLargest(nums, k))
