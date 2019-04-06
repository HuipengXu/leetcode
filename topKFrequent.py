# @Time    : 2019/4/6 13:29
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Tuple
from collections import defaultdict
import heapq


# 堆，O(nlogn)
def topKFrequent0(nums: List[int], k: int) -> List[int]:
    counts = defaultdict(int)
    for elem in nums:
        counts[elem] += 1
    big_heap = []
    for elem, freq in counts.items():
        heapq.heappush(big_heap, (-freq, elem))
    return [heapq.heappop(big_heap)[1] for _ in range(k)]


# 归并排序
def merge_sort(nums: List[Tuple[int, int]]) -> None:
    def merge_sort_c(nums: List[Tuple[int, int]], start: int, end: int) -> None:
        if end - start <= 1: return
        mid = start + ((end - start) >> 1)
        merge_sort_c(nums, start, mid)
        merge_sort_c(nums, mid, end)
        merge(nums, start, mid, end)

    def merge(nums: List[Tuple[int, int]], start: int, mid: int, end: int) -> None:
        i, j, k = start, mid, 0
        temp = [(0, 0)] * (end - start)
        while i < mid and j < end:
            if nums[i][1] <= nums[j][1]:
                temp[k] = nums[i]
                k += 1
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
                k += 1
        if i == mid:
            while j < end:
                temp[k] = nums[j]
                k += 1
                j += 1
        elif j == end:
            while i < mid:
                temp[k] = nums[i]
                k += 1
                i += 1
        for m in range(end - start):
            nums[m + start] = temp[m]

    merge_sort_c(nums, 0, len(nums))


def topKFrequent1(nums: List[int], k: int) -> List[int]:
    counts = defaultdict(int)
    for elem in nums:
        counts[elem] += 1
    counts_sorted = list(counts.items())
    merge_sort(counts_sorted)
    return [counts_sorted[-i][0] for i in range(1, k + 1)]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
    print(topKFrequent0(nums, 2))
    print(topKFrequent1(nums, 2))
