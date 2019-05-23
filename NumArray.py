# @Time    : 2019/5/23 20:35
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            self.sums.append(sum_)

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]
