# @Time    : 2019/4/3 20:58
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ret = self.nums.copy()
        for i in range(len(ret)):
            j = random.randint(i, len(ret) - 1)
            ret[i], ret[j] = ret[j], ret[i]
        return ret
