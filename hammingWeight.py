# @Time    : 2019/6/6 13:37
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    def hammingWeight1(self, n):
        res = 0
        while n:
            n, remainder = divmod(n, 2)
            if remainder == 1: res += 1
        return res

    def hammingWeight2(self, n):
        res = 0
        while n:
            cur_bit = n & 1
            if cur_bit == 1: res += 1
            n >>= 1
        return res
