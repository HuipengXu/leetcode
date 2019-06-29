# @Time    : 2019/6/29 8:37
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            tmp = numbers[low] + numbers[high]
            if tmp > target:
                high -= 1
            elif tmp < target:
                low += 1
            else:
                return [low + 1, high + 1]
        return [-1, -1]
