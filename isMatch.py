# @Time    : 2019/5/18 15:11
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = False
        # 记录是否访问过
        visited = set()

        def back_tracking(i: int, j: int) -> None:
            nonlocal match
            if (i, j) in visited: return
            visited.add((i, j))
            if match: return
            if j == len(p):
                if i == len(s):
                    match = True
                return
            if p[j] == '*':
                if j - 1 >= 0 and i < len(s) and (p[j - 1] == s[i] or p[j - 1] == '.'):
                    back_tracking(i + 1, j + 1)
                    back_tracking(i + 1, j)
                back_tracking(i, j + 1)
            if p[j] == '.' or i < len(s) and p[j] == s[i]:
                back_tracking(i + 1, j + 1)
            if j + 1 < len(p) and p[j + 1] == '*':
                back_tracking(i, j + 1)

        back_tracking(0, 0)
        return match


#     dp 解法：https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest


if __name__ == '__main__':
    # s = "kjjkaaaan"
    # p = "**.j*k*a.a*."
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*c"
    so = Solution()
    print(so.isMatch(s, p))
