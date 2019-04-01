# @Time    : 2019/3/31 22:05
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
import sys


def maxProduct(nums: List[int]) -> int:
    if len(nums) == 0: return 0
    max_product = -int(sys.maxsize)
    for i in range(len(nums)):
        product = nums[i]
        if product > max_product:
            max_product = product
        for j in range(i + 1, len(nums)):
            product *= nums[j]
            if product > max_product:
                max_product = product
    return max_product


def super_max_product(nums: List[int]) -> int:
    length = len(nums)
    if length == 0: return 0
    states = [{nums[i]} for i in range(length)]
    for j in range(1, length):
        for p in states[j - 1]:
            states[j].add(p * nums[j])
    return max(p for l in states for p in l)


def dp_max_product(nums: List[int]) -> int:
    length = len(nums)
    if length == 0: return 0
    dp = maxm = minm = nums[0]
    for i in range(1, length):
        if nums[i] >= 0:
            maxm = max(maxm * nums[i], nums[i])
            minm = min(minm * nums[i], nums[i])
        else:
            tmp = maxm
            maxm = max(minm * nums[i], nums[i])
            minm = min(tmp * nums[i], nums[i])
        dp = max(dp, maxm)
    return dp


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    # nums = [-2, 0, -1]
    # nums = []
    print(maxProduct(nums))
    print(super_max_product(nums))
