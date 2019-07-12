# @Time    : 2019/7/12 18:31
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(i: int, tmp: List[int]) -> None:
            if sum(tmp) > n: return
            if len(tmp) == k:
                if sum(tmp) == n:
                    res.append(tmp)
                return
            for j in range(i, 10):
                dfs(j + 1, tmp + [j])

        dfs(1, [])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 9))
