# @Time    : 2019/4/4 16:17
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    cumprods = [0] * length
    reversed_cumprods = [0] * length
    prod = 1
    for i in range(length):
        prod *= nums[i]
        cumprods[i] = prod
    prod = 1
    for j in range(length - 1, -1, -1):
        prod *= nums[j]
        reversed_cumprods[j] = prod
    ret = [0] * length
    for k in range(length):
        left = cumprods[k - 1] if k - 1 >= 0 else 1
        right = reversed_cumprods[k + 1] if k + 1 < length else 1
        ret[k] = left * right
    return ret


def super_productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    ret = [0] * length
    ret[-1] = nums[-1]
    for i in range(length - 2, -1, -1):
        ret[i] = ret[i + 1] * nums[i]
    ret[0] = ret[1]
    for j in range(1, length):
        nums[j] = nums[j] * nums[j - 1]
        right = ret[j + 1] if j + 1 < length else 1
        ret[j] = nums[j - 1] * right
    return ret


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(super_productExceptSelf(a))
