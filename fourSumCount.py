# @Time    : 2019/4/10 21:18
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import defaultdict


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum_ab = defaultdict(int)
        for a in A:
            for b in B:
                sum_ab[a + b] += 1
        count = 0
        for c in C:
            for d in D:
                if sum_ab[-(c + d)] > 0:
                    count += sum_ab[-(c + d)]
        return count
