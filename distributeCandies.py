# @Time    : 2019/6/13 10:17
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import defaultdict


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candy_cnt = defaultdict(int)
        for c in candies:
            candy_cnt[c] += 1
        kinds = len(candy_cnt)
        all_candies = len(candies)
        return kinds if all_candies // 2 > kinds else all_candies // 2

    def distributeCandies1(self, candies: List[int]) -> int:
        kinds = len(set(candies))
        cnt = len(candies)
        return kinds if cnt // 2 > kinds else cnt // 2
