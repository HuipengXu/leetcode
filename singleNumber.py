# @Time    : 2019/2/28 20:21
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
"""
只出现一次的数字：
https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/261/before-you-start/1106/

异或
0 和其他数字异或为本身，相同的两个数异或为 0
"""
from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0
    for i in nums:
        res ^= i
    return res
