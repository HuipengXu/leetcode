# @Time    : 2019/5/27 18:46
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return [1]
        res = [0] * (len(digits) + 1)
        carry, num = divmod(digits[-1] + 1, 10)
        res[-1] = num
        for i in range(len(digits) - 2, -1, -1):
            carry, num = divmod(digits[i] + carry, 10)
            res[i + 1] = num
        if carry != 0:
            res[0] = carry
            return res
        return res[1:]


if __name__ == '__main__':
    s = Solution()
    nums = [9, 9, 9]
    print(s.plusOne(nums))
