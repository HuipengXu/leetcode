# @Time    : 2019/4/20 22:06
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        pre_pre = pre = current = 0
        for i in range(1, len(nums) + 1):
            current = max(pre, pre_pre + nums[i - 1])
            pre_pre = pre
            pre = current
        return current

    def rob1(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def recur(nums: List[int], i: int) -> int:
            if i < 0: return 0
            if memo[i] != -1:
                return memo[i]
            return max(recur(nums, i - 1), recur(nums, i - 2) + nums[i])

        return recur(nums, len(nums) - 1)


if __name__ == '__main__':
    a = [3, 2, 1, 4, 5, 6]
    s = Solution()
    print(s.rob(a))
    print(s.rob1(a))
