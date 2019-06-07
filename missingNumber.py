# @Time    : 2019/6/7 8:28
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i != nums[i] and nums[i] < len(nums):
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
        for i in range(len(nums)):
            if i != nums[i]:
                return i

    def missingNumber1(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i
        return res

    def missingNumber2(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(s.missingNumber(nums))
