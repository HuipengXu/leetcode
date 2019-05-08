# @Time    : 2019/1/23 14:27
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

"""
4. 寻找两个有序数组的中位数
时间复杂度为 O(m+n)，未达到题目要求 O(log(m+n))
"""
from typing import List


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

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = k = 0
        total_length = len(nums1) + len(nums2)
        tmp = [0] * (total_length // 2 + 1)
        flag = True if total_length % 2 else False
        while k <= total_length // 2 and i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                tmp[k] = nums1[i]
                i += 1
            else:
                tmp[k] = nums2[j]
                j += 1
            k += 1
        while k <= total_length // 2:
            if i < len(nums1):
                tmp[k] = nums1[i]
                k += 1
                i += 1
            else:
                tmp[k] = nums2[j]
                k += 1
                j += 1
        return tmp[-1] if flag else (tmp[-1] + tmp[-2]) / 2

    # 参考答案
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        shorter_nums, longer_nums = nums1, nums2 if len(nums1) <= len(nums2) else (nums2, nums1)
        s_len, l_len = len(shorter_nums), len(longer_nums)
        s, t = 0, s_len
        while s <= t:
            i = s + ((t - s) >> 1)
            j = (s_len + l_len + 1) // 2 - i
            if i < s_len and longer_nums[j - 1] > shorter_nums[i]:
                s = i + 1
            elif i > 0 and shorter_nums[i - 1] > longer_nums[j]:
                t = i
            else:
                if i == 0:
                    max_of_left = longer_nums[j - 1]
                elif j == 0:
                    max_of_left = shorter_nums[i - 1]
                else:
                    max_of_left = max(longer_nums[j - 1], shorter_nums[i - 1])
                if (s_len + l_len) % 2:
                    return max_of_left
                if i == s_len:
                    min_of_right = longer_nums[j]
                elif j == l_len:
                    min_of_right = shorter_nums[i]
                else:
                    min_of_right = min(longer_nums[j], shorter_nums[i])
                return (min_of_right + max_of_left) / 2.0
