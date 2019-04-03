# @Time    : 2019/4/3 15:55
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


def moveZeroes0(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0: return
    not_zero = None
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            not_zero = i
            break
    if not_zero is None: return
    k = not_zero
    for j in range(not_zero - 1, -1, -1):
        if nums[j] == 0:
            for m in range(j, k):
                nums[m], nums[m + 1] = nums[m + 1], nums[m]
            k -= 1


def moveZeroes1(nums: List[int]) -> None:
    if len(nums) == 0: return
    idx = 0
    for d in nums:
        if d != 0:
            nums[idx] = d
            idx += 1
    for i in range(idx, len(nums)):
        nums[i] = 0


def moveZeroes2(nums: List[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 2, 0, 3, 0, 5, 6]
    moveZeroes2(nums)
    print(nums)
