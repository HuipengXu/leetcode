# @Time    : 2019/6/21 7:36
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            pre = 1
            for j in range(1, i):
                tmp = res[j]
                res[j] += pre
                pre = tmp
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(0))
