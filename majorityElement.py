# @Time    : 2019/2/28 20:40
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
"""
求众数
https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/261/before-you-start/1107/
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    nums2freq = {}
    for i in nums:
        if i not in nums2freq:
            nums2freq[i] = 1
        else:
            nums2freq[i] += 1
        if nums2freq[i] > len(nums) // 2:
            return i
