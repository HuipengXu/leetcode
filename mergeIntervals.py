# @Time    : 2019/5/12 7:56
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1: return []
        intervals.sort(key=lambda x: x[0])
        ret = []
        pointer = 1
        left, right = intervals[0][0], intervals[0][1]
        while pointer < len(intervals):
            while pointer < len(intervals) and intervals[pointer][0] <= right:
                right = max(intervals[pointer][-1], right)
                pointer += 1
            ret.append([left, right])
            if pointer < len(intervals):
                left, right = intervals[pointer][0], intervals[pointer][1]
            pointer += 1
        if pointer == len(intervals): ret.append([left, right])
        return ret

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        for item in sorted(intervals, key=lambda x: x[0]):
            if ret and ret[-1][-1] >= item[0]:
                ret[-1][-1] = max(ret[-1][-1], item[-1])
            else:
                ret.append(item)
        return ret


if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 4], [2, 3], [0, 9]]
    print(s.merge(intervals))
    print(s.merge1(intervals))
