# @Time    : 2019/6/4 10:13
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(s.removeDuplicates(nums))
