# @Time    : 2019/5/27 13:50
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums_set = {num for num in nums if num > 0}
        while nums_set:
            num = nums_set.pop()
            if res == num:
                res += 1
                while res in nums_set:
                    nums_set.remove(res)
                    res += 1
        return res

    def firstMissingPositive1(self, nums: List[int]) -> int:
        i = 1
        nums = set(nums)
        while i in nums:
            i += 1
        return i

    def firstMissingPositive2(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while 0 < nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1


if __name__ == '__main__':
    s = Solution()
    # nums = [1,2,3,4,5,6,7]
    nums = [0, 2, 1]
    print(s.firstMissingPositive2(nums))
