# @Time    : 2019/6/27 10:23
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import Counter, defaultdict
from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache()
        def helper(s1: str, s2: str) -> bool:
            if s1 == s2: return True
            if len(s1) != len(s2) or sorted(s1) != sorted(s2):
                return False
            for i in range(1, len(s1)):
                if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                    return True
                if helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i]):
                    return True
            return False

        return helper(s1, s2)

    def isScramble1(self, s1: str, s2: str) -> bool:
        memo = {}

        def helper(s1: str, s2: str) -> bool:
            res = memo.get((s1, s2), -1)
            if res == 1:
                return True
            elif res == 0:
                return False
            if s1 == s2:
                memo[(s1, s2)] = 1
                return True
            if len(s1) != len(s2) or sorted(s1) != sorted(s2):
                memo[(s1, s2)] = 0
                return False
            for i in range(1, len(s1)):
                if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                    memo[(s1, s2)] = 1
                    return True
                if helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = 1
                    return True
            memo[(s1, s2)] = 0
            return False

        return helper(s1, s2)
