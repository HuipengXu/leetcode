# @Time    : 2019/6/13 10:55
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cumulative = [0]
        for i in nums:
            cumulative.append(cumulative[-1] + i)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if cumulative[j] - cumulative[i] == k:
                    res += 1
        return res

    def subarraySum1(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            sum_ = 0
            for j in range(i, len(nums)):
                sum_ += nums[j]
                if sum_ == k: res += 1
        return res

    def subarraySum2(self, nums: List[int], k: int) -> int:
        res = 0
        sum_ = defaultdict(int)
        sum_[0] = 1
        cumulative = 0
        for num in nums:
            cumulative += num
            if cumulative - k in sum_:
                res += sum_[cumulative - k]
            sum_[cumulative] += 1
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.subarraySum(nums, 2))
    print(s.subarraySum1(nums, 2))
