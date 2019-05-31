# @Time    : 2019/5/31 19:07
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
import sys


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: return []
        res = [0] * len(T)
        stack = [0]
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        if not T: return []
        res = [sys.maxsize] * len(T)
        res[-1] = 0
        temp_hash = {T[-1]: len(T) - 1}
        for i in range(len(T) - 2, -1, -1):
            for t in range(T[i] + 1, 101):
                if t in temp_hash:
                    idx = temp_hash[t]
                    res[i] = min(idx - i, res[i])
            if res[i] == sys.maxsize: res[i] = 0
            temp_hash[T[i]] = i
        return res
