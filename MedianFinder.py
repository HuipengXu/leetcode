# @Time    : 2019/4/5 10:31
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap = []
        self.small_heap = []

    def addNum(self, num: int) -> None:
        if len(self.big_heap) == len(self.small_heap):
            heapq.heappush(self.big_heap, - heapq.heappushpop(self.small_heap, num))
        else:
            heapq.heappush(self.small_heap, - heapq.heappushpop(self.big_heap, -num))

    def findMedian(self) -> Optional[float]:
        if len(self.big_heap) == len(self.small_heap):
            left = - self.big_heap[0]
            right = self.small_heap[0]
            return (left + right) / 2
        else:
            return - self.big_heap[0]


if __name__ == "__main__":
    mf = MedianFinder()
    for num in [9, 2, 1, 4, 9, 6]:
        mf.addNum(num)
    print(mf.findMedian())
