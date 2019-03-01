# @Time    : 2019/3/1 14:45
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

"""
合并两个有序数组
https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/261/before-you-start/1109/
"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if len(nums1) == 0 or len(nums2) == 0: return None
    j = 0
    while j < m:
        if nums1[j] <= nums2[0]:
            j += 1
        else:
            nums1[j], nums2[0] = nums2[0], nums1[j]
            k = 0
            while k < n - 1 and nums2[k] > nums2[k + 1]:
                nums2[k], nums2[k + 1] = nums2[k + 1], nums2[k]
                k += 1
    nums1[m:] = nums2[:]
