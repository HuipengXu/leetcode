# @Time    : 2019/6/2 15:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        i = 0
        while i < len(nums) - 2:
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < len(nums) - 1:
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] < target:
                        continue
                    tmp = float('inf')
                    cur = nums[i] + nums[j] + nums[k]
                    if k - 1 >= j + 1: tmp = nums[i] + nums[j] + nums[k - 1]
                    if abs(target - tmp) < abs(closest - target): closest = tmp
                    if cur - target < abs(closest - target): closest = cur
                    break
                else:
                    cur = nums[i] + nums[j] + nums[-1]
                    if target - cur < abs(closest - target): closest = cur
                j += 1
            i += 1
        return closest

    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur == target: return target
                if abs(closest - target) > abs(cur - target):
                    closest = cur
                elif cur > target:
                    k -= 1
                else:
                    j += 1
        return closest


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 1]
    print(s.threeSumClosest(nums, 0))
