# @Time    : 2019/4/4 20:31
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxsize

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        if len(self.stack) == 0: return
        top = self.stack.pop()
        if len(self.stack) == 0:
            self.min = sys.maxsize
            return
        if top == self.min:
            self.min = self.stack[-1]
            for i in range(len(self.stack) - 1):
                if self.stack[i] < self.min:
                    self.min = self.stack[i]

    def top(self) -> int:
        if len(self.stack) == 0: return -1
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
