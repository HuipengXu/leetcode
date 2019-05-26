# @Time    : 2019/5/26 19:38
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 0
        while fast < len(nums):
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1
            slow += 1
            if fast >= len(nums): break
            nums[slow] = nums[fast]
        return slow

    def removeDuplicates1(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
