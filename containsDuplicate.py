# @Time    : 2019/4/3 13:36
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import defaultdict
from typing import List
import random

"""
采用字典记录元素的个数
时间复杂度最糟糕的情况为 O(n)，平均应该更小；空间复杂度为 O(n)
"""


def containsDuplicate0(nums: List[int]) -> bool:
    counts = defaultdict(int)
    for i in nums:
        counts[i] += 1
        if counts[i] > 1:
            return True
    return False


"""
采用快排
时间复杂度 O(nlogn)，空间复杂度 O(1)
居然超出时间限制
"""


def quick_sort(nums: List[int]) -> None:
    def partition(nums: List[int], start: int, end: int):
        if end - start <= 1: return
        # 随机选取分割点，防止有序数组造成性能退化
        pivot_idx = random.randint(start, end - 1)
        nums[end - 1], nums[pivot_idx] = nums[pivot_idx], nums[end - 1]
        j = start
        for i in range(start, end):
            if nums[i] <= nums[end - 1]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j

    def quick_sort_c(nums: List[int], start: int, end: int):
        mid = partition(nums, start, end)
        if mid is None: return
        quick_sort_c(nums, start, mid - 1)
        quick_sort_c(nums, mid, end)

    quick_sort_c(nums, 0, len(nums))


def containsDuplicate1(nums: List[int]) -> bool:
    quick_sort(nums)
    print(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


if __name__ == "__main__":
    a = [1, 2, 3, 1]
    ret = containsDuplicate1(a)
    print(ret)
