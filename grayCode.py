# @Time    : 2019/6/3 9:31
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # 超过最大递归深度
    def grayCode(self, n: int) -> List[int]:
        res = []
        flag = False

        def back_tracking(cur: str, tmp: list, visited: set) -> None:
            nonlocal flag
            if flag: return
            if len(tmp) == 2 ** n:
                flag = True
                res.extend(tmp)
                return
            if cur in visited: return
            for i in range(len(cur)):
                replace = '0' if cur[i] == '1' else '1'
                back_tracking(cur[:i] + replace + cur[i + 1:], tmp + [int(cur, 2)], visited | {cur})

        back_tracking('0' * n, [], set())
        return res

    def grayCode1(self, n: int) -> List[int]:
        res = []
        for i in range(2 ** n):
            res.append(i ^ (i // 2))
        return res

    def grayCode2(self, n: int) -> List[int]:
        if n == 0: return [0]

        def dp(n: int) -> List[int]:
            if n == 1: return [0, 1]
            pre = dp(n - 1)
            cur = []
            for i in range(len(pre) - 1, -1, -1):
                cur.append(2 ** (n - 1) + pre[i])
            return pre + cur

        return dp(n)


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode1(11))
