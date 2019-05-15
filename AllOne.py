# @Time    : 2019/5/15 14:25
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import defaultdict


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = defaultdict(int)
        self.nums = [set()]
        # self.min_idx = 0

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.keys[key] += 1
        if self.keys[key] - 2 >= 0:
            self.nums[self.keys[key] - 2].remove(key)
        if self.keys[key] > len(self.nums):
            self.nums.append({key})
        else:
            self.nums[self.keys[key] - 1].add(key)
        # if len(self.nums[self.min_idx]) == 0 and len(self.nums[0]) == 0:
        #     self.min_idx += 1
        # elif len(self.nums[0]) >= 1:
        #     self.min_idx = 0

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if self.keys[key] >= 1: self.nums[self.keys[key] - 1].remove(key)
        if self.keys[key] > 1:
            self.keys[key] -= 1
            self.nums[self.keys[key] - 1].add(key)
        elif self.keys[key] == 1:
            del self.keys[key]
        if len(self.nums[-1]) == 0 and len(self.nums) > 1: self.nums.pop()
        # if self.min_idx > 0 and len(self.nums[self.min_idx-1]) > 0:
        #     self.min_idx -= 1

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        for max_ in self.nums[-1]:
            return max_
        return ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        for s in self.nums:
            for min_ in s:
                return min_
        return ''


if __name__ == '__main__':
    ao = AllOne()
    # ao.inc('bi')
    # ao.inc('xing')
    # ao.inc('bi')
    # ao.inc('feng')
    # ao.inc('xing')
    # ao.dec('xing')
    # print(ao.getMaxKey())
    # print(ao.getMinKey())
    ao.inc('a')
    ao.inc('b')
    ao.inc('b')
    ao.inc('c')
    ao.inc('c')
    ao.inc('c')
    ao.dec('b')
    ao.dec('b')
    print(ao.getMinKey())
    ao.dec('a')
    print(ao.getMaxKey())
    print(ao.getMinKey())
