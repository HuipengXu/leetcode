# @Time    : 2019/5/11 14:53
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        length = len(nums)
        for i in range(1, length - 1):
            right = length - 1
            left = 0 if nums[i] != nums[i - 1] else i - 1
            if nums[i] == nums[i - 1]: left = i - 1
            while left < i and right > i:
                tmp_sum = nums[left] + nums[i] + nums[right]
                if tmp_sum == 0:
                    ret.add((nums[left], nums[i], nums[right]))
                    left += 1
                    while left < i and nums[left] == nums[left - 1]:
                        left += 1
                elif tmp_sum > 0:
                    right -= 1
                else:
                    left += 1
        return list(map(list, ret))

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp_sum = nums[i] + nums[left] + nums[right]
                if tmp_sum > 0:
                    right -= 1
                elif tmp_sum < 0:
                    left += 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0, 0]
    print(s.threeSum(nums))
    print(s.threeSum1(nums))
