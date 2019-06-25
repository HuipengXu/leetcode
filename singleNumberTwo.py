# @Time    : 2019/6/25 13:36
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones

    def singleNumber1(self, nums: List[int]) -> int:
        """负数不行"""
        res = 0
        for i in range(32):
            sum = 0
            for num in nums:
                sum += (num >> i) & 1
            res |= sum % 3 << i
        return res

    def singleNumber2(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = b ^ num & ~a
            a = a ^ num & ~b
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 3, 2]))
    print(s.singleNumber1([2, 2, 3, 2]))
