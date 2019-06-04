# @Time    : 2019/6/4 17:07
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = sum_ = 0
        for right in range(len(nums)):
            sum_ += nums[right]
            while sum_ >= s:
                min_len = min(right - left + 1, min_len)
                sum_ -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    print(s.minSubArrayLen(7, nums))
