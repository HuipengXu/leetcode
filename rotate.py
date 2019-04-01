# @Time    : 2019/4/1 13:44
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from typing import List


# 超出时间限制
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    start = len(nums) - k
    for i in range(k):
        for j in range(start + i, i, -1):
            nums[j], nums[j - 1] = nums[j - 1], nums[j]


def super_rotate0(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def rotate(nums, s, k):
        length = len(nums[s:])
        k %= length
        start = length - k + s
        j = s
        for i in range(start, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        left = length - k
        move = k % left
        if move == 0:
            return
        else:
            rotate(nums, s + k, move)

    rotate(nums, 0, k)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    super_rotate0(nums, 3)
    print(nums)
