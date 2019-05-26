# @Time    : 2019/5/26 9:39
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from random import randint


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                pointer = i

        def quick_sort(start: int, end: int):
            if end - start <= 0: return

            def partition(start, end) -> int:
                idx = randint(start, end)
                nums[idx], nums[end] = nums[end], nums[idx]
                j = start
                for i in range(start, end + 1):
                    if nums[i] <= nums[end]:
                        nums[i], nums[j] = nums[j], nums[i]
                        j += 1
                return j - 1

            j = partition(start, end)
            quick_sort(start, j - 1)
            quick_sort(j + 1, end)

        quick_sort(pointer, len(nums) - 1)
        for i in range(pointer, len(nums)):
            if nums[i] > nums[pointer - 1]:
                nums[i], nums[pointer - 1] = nums[pointer - 1], nums[i]
                return

    def nextPermutation1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
        m, n = i + 1, len(nums) - 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 5]
    print(s.nextPermutation(nums))
    print(nums)
