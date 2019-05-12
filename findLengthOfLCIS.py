# @Time    : 2019/5/12 15:15
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        prev = 1
        max_len = 0
        for i in range(1, len(nums)):
            current = 1
            if nums[i] > nums[i - 1]:
                current = prev + 1
                max_len = max(max_len, current)
            prev = current
        return max_len


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 3, 4, 6, 9]
    print(s.findLengthOfLCIS(nums))
