# @Time    : 2019/5/26 8:27
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = {''}
        for i in range(n):
            tmp = set()
            for p in res:
                for j in range(0, 2 * len(p) + 1, 2):
                    new_par = p[:j // 2] + '()' + p[j // 2:]
                    tmp.add(new_par)
            res = tmp
        return list(res)

    def generateParenthesis1(self, n: int) -> List[str]:
        res = []

        def back_tracking(cur: str, open: int, close: int):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if open < n:
                back_tracking(cur + '(', open + 1, close)
            if close < open:
                back_tracking(cur + ')', open, close + 1)

        back_tracking('', 0, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis1(3))
