# @Time    : 2019/1/23 14:27
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

"""
4. 寻找两个有序数组的中位数
时间复杂度为 O(m+n)，未达到题目要求 O(log(m+n))
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        l = l1 + l2
        i = j = k = 0
        new_nums = [0] * l
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                new_nums[k] = nums1[i]
                i += 1
            else:
                new_nums[k] = nums2[j]
                j += 1
            k += 1
        start, tmp_nums = (i, nums1) if i < l1 else (j, nums2)
        new_nums[k:] = tmp_nums[start:]
        if l % 2:
            return new_nums[int((l - 1) / 2)]
        else:
            return (new_nums[int(l / 2)] + new_nums[int(l / 2) - 1]) / 2
