# @Time    : 2019/4/10 21:50
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from random import randint


class RandomizedSet0:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data: return False
        self.data[val] = val
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data: return False
        self.data.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        keys = list(self.data.keys())  # 这里时间复杂度貌似为 O(n)，不符合
        idx = randint(0, len(keys) - 1)
        return keys[idx]


class RandomizedSet1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos: return False
        self.data.append(val)
        self.pos[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos: return False
        idx, last = self.pos[val], self.data[-1]
        self.data[idx] = last
        self.pos[last] = idx
        self.data.pop()
        self.pos.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = randint(0, len(self.data) - 1)
        return self.data[idx]
