# @Time    : 2019/4/3 21:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import defaultdict


# 无序
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_counts = defaultdict(int)
    nums2_counts = defaultdict(int)
    for num in nums1:
        nums1_counts[num] += 1
    for num in nums2:
        nums2_counts[num] += 1
    ret = []

    def get_intersect(less_nums: dict, more_nums: dict):
        for num, count in less_nums.items():
            num2_count = more_nums.get(num, 0)
            intersect_count = min(count, num2_count)
            for _ in range(intersect_count):
                ret.append(num)

    if len(set(nums1)) < len(set(nums2)):
        get_intersect(nums1_counts, nums2_counts)
    else:
        get_intersect(nums2_counts, nums1_counts)
    return ret


# 无序
def intersect1(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_counts = defaultdict(int)
    for num in nums1:
        nums1_counts[num] += 1
    ret = []
    for num in nums2:
        if nums1_counts.get(num, 0) != 0:
            ret.append(num)
            nums1_counts[num] -= 1
    return ret


# 有序
def intersect_sorted(nums1: List[int], nums2: List[int]) -> List[int]:
    i = j = 0
    len1, len2 = len(nums1), len(nums2)
    ret = []
    while i < len1 and j < len2:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            while i < len1 and j < len2 \
                    and nums1[i] == nums2[j]:
                ret.append(nums1[i])
                i += 1
                j += 1
    return ret


if __name__ == "__main__":
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersect1(nums1, nums2))
    print(intersect_sorted(sorted(nums1), sorted(nums2)))
