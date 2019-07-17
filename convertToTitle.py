# @Time    : 2019/7/17 14:15
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import deque


class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = deque()
        while n > 0:
            n -= 1
            n, remainder = divmod(n, 26)
            ans.appendleft(chr(remainder + 65))
        return ''.join(ans)
