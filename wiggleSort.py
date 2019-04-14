# @Time    : 2019/4/14 9:14
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from typing import List
from random import randint


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge_sort_c(nums: List[int], start: int, end: int):
            if end - start <= 1: return
            mid = start + ((end - start) >> 1)
            merge_sort_c(nums, start, mid)
            merge_sort_c(nums, mid, end)
            merge(nums, start, mid, end)

        def merge(nums: List[int], start: int, mid: int, end: int) -> None:
            i, j, k = start, mid, 0
            tmp = [0] * (end - start)
            while i < mid and j < end:
                if nums[i] <= nums[j]:
                    tmp[k] = nums[i]
                    i += 1
                else:
                    tmp[k] = nums[j]
                    j += 1
                k += 1
            if i == mid:
                tmp[k:] = nums[j: end]
            else:
                tmp[k:] = nums[i: mid]
            nums[start: end] = tmp[:]

        def wiggle(nums: List[int]) -> list:
            ret = [0] * len(nums)
            mid = (len(nums) + 1) // 2
            if mid == len(nums): return nums
            i, j, k, flag = mid - 1, len(nums) - 1, 0, True
            while i >= 0 or j >= mid:
                if flag:
                    ret[k] = nums[i]
                    i -= 1
                    flag = False
                else:
                    ret[k] = nums[j]
                    j -= 1
                    flag = True
                k += 1
            return ret

        merge_sort_c(nums, 0, len(nums))
        ret = wiggle(nums)
        nums[:] = ret[:]


if __name__ == "__main__":
    s = Solution()
    # nums = [2, 4, 4, 6, 7, 7, 8]
    nums = [4, 5, 5, 6]
    s.wiggleSort(nums)
    print(nums)
