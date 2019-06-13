# @Time    : 2019/6/13 8:01
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, length = [], len(nums)
        for i in range(length - 3):
            if (i >= 1 and nums[i] == nums[i - 1] or
                    nums[i] + nums[length - 1] + nums[length - 2] + nums[length - 3] < target): continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target: break
            for j in range(i + 1, length - 2):
                if (j >= i + 2 and nums[j] == nums[j - 1] or
                        nums[i] + nums[j] + nums[length - 1] + nums[length - 2] < target): continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: break
                temp = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == temp:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > temp:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
