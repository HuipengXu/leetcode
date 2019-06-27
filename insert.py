# @Time    : 2019/6/27 8:02
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res, i = [], 0
        while i < len(intervals):
            if end < intervals[i][0]:
                res.append([start, end])
                res.append(intervals[i])
                break
            elif intervals[i][0] <= end <= intervals[i][-1]:
                if start < intervals[i][0]:
                    res.append([start, intervals[i][-1]])
                else:
                    res.append(intervals[i])
                break
            elif intervals[i][0] <= start <= intervals[i][-1]:
                start = intervals[i][0]
            elif start > intervals[i][-1]:
                res.append(intervals[i])
            i += 1
        else:
            res.append([start, end])
        return res + intervals[i + 1:]

    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        left = [i for i in intervals if i[-1] < s]
        right = [i for i in intervals if i[0] > e]
        if len(left) + len(right) < len(intervals):
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][-1])
        return left + [[s, e]] + right
