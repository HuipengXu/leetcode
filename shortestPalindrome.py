# @Time    : 2019/7/5 11:40
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        dp = [{0, 1}]
        for i in range(1, len(s)):
            dp.append({i, i + 1})
            for j in dp[i - 1]:
                if j - 1 >= 0 and s[i] == s[j - 1]:
                    dp[i].add(j - 1)
        j = len(s) - 1
        while j >= 0:
            if 0 in dp[j]:
                break
            j -= 1
        return s[j + 1:][::-1] + s

    def shortestPalindrome1(self, s: str) -> str:
        def is_palindrome(s: str) -> bool:
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = len(s)
        while i >= 0:
            if is_palindrome(s[:i]):
                break
            i -= 1
        return s[i:][::-1] + s

    def shortestPalindrome2(self, s: str) -> str:
        def get_next(s: str) -> List[int]:
            next_ = [-1]
            for i in range(1, len(s)):
                j = next_[i - 1]
                while j >= 0 and s[i] != s[j + 1]:
                    j = next_[j]
                j = j + 1 if s[i] == s[j + 1] else -1
                next_.append(j)
            return next_[-1]

        new_s = s + '#' + s[::-1]
        j = get_next(new_s)
        return s[j + 1:][::-1] + s


if __name__ == '__main__':
    s = Solution()
    ss = ''
    print(s.shortestPalindrome(ss))
