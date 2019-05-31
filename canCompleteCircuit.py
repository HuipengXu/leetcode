# @Time    : 2019/5/31 14:11
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            j = (i + 1) % len(gas)
            g = gas[i]
            while j != i:
                dec = cost[j - 1] if j - 1 >= 0 else cost[-1]
                if g < dec: break
                g = g + gas[j] - dec
                j = (j + 1) % len(gas)
            if j == i:
                dec = cost[j - 1] if j - 1 >= 0 else cost[-1]
                if g >= dec: return i
        return -1

    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        remain_gas = [(gas[i] - cost[i], i) for i in range(len(gas)) if gas[i] - cost[i] >= 0]
        remain_gas.sort(key=lambda x: x[0], reverse=True)
        for _, i in remain_gas:
            j = (i + 1) % len(gas)
            g = gas[i]
            while j != i:
                dec = cost[j - 1] if j - 1 >= 0 else cost[-1]
                if g < dec: break
                g = g + gas[j] - dec
                j = (j + 1) % len(gas)
            if j == i:
                dec = cost[j - 1] if j - 1 >= 0 else cost[-1]
                if g >= dec: return i
        return -1

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        start = run = rest = 0
        for i in range(len(gas)):
            run += (gas[i] - cost[i])
            rest += (gas[i] - cost[i])
            if run < 0:
                start = i + 1
                run = 0
        return start if rest >= 0 else -1
