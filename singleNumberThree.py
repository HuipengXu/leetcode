# @Time    : 2019/7/20 15:25
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tmp = 0
        for num in nums:
            tmp ^= num
        mask = tmp & (-tmp)
        ans = [0, 0]
        for num in nums:
            if num & mask == 0:
                ans[0] ^= num
            else:
                ans[1] ^= num
        return ans
