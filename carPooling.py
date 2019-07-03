# @Time    : 2019/7/3 20:27
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        off_dist = []
        count = 0
        for i in range(len(trips)):
            dist = trips[i][1]
            while off_dist and dist >= off_dist[0][0]:
                _, passenger = heapq.heappop(off_dist)
                count -= passenger
            count += trips[i][0]
            if count > capacity:
                return False
            heapq.heappush(off_dist, [trips[i][-1], trips[i][0]])
        return True

    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        stop = []
        for n, s, e in trips:
            stop.append([s, n])
            stop.append([e, -n])

        stop.sort()

        for _, count in stop:
            capacity -= count
            if capacity < 0: return False

        return True
