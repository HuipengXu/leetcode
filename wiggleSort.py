# @Time    : 2019/4/14 9:14
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from typing import List, Optional


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

    def super_wiggle_sort(self, nums: List[int]) -> None:
        def findKthLargest(nums: List[int], k: int) -> Optional[int]:
            if k > len(nums) or k <= 0:
                return None

            def partition(nums: list, p: int, r: int):
                pivot = nums[r - 1]
                i = p
                for j in range(p, r):
                    if nums[j] >= pivot:
                        nums[j], nums[i] = nums[i], nums[j]
                        i += 1
                return i

            p = 0
            r = len(nums)
            while True:
                q = partition(nums, p, r)
                if q == k:
                    return
                elif q > k:
                    p = 0
                    r = q - 1
                else:
                    p = q
                    r = len(nums)

        mid = (len(nums) + 1) // 2
        findKthLargest(nums, mid)
        median = nums[mid - 1]
        re_index = lambda x: (1 + 2 * x) % (len(nums) | 1)
        # 这块索引的变换真的搞不太懂
        i = j = 0
        k = len(nums) - 1
        while j <= k:
            # 大于中位数的放到奇数位
            if nums[re_index(j)] > median:
                nums[re_index(i)], nums[re_index(j)] = nums[re_index(j)], nums[re_index(i)]
                i += 1
                j += 1
            # 小于中位数的放到偶数位
            elif nums[re_index(j)] < median:
                nums[re_index(j)], nums[re_index(k)] = nums[re_index(k)], nums[re_index(j)]
                k -= 1
            else:
                j += 1


if __name__ == "__main__":
    s = Solution()
    nums = [2, 4, 4, 6, 7, 7, 8]
    # nums = [4, 5, 5, 6]
    # s.wiggleSort(nums)
    s.super_wiggle_sort(nums)
    print(nums)
