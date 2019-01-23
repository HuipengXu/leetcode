# @Time    : 2019/1/23 20:04
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
"""
5. 最长回文子串
"""


class Solution:
    """
    巨丑的代码。。。。
    算了，好歹是自己想出来的
    """

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        longest_p = longest_q = 0
        length = len(s)
        for i in range(1, length):
            # 应对 "ccc"
            again = False
            if (i + 1) < length and s[i] == s[i - 1] == s[i + 1]:
                again = True
            # 应对 "beef"
            if s[i] == s[i - 1]:
                p = i - 1
                q = i
            # 应对 "eye"
            else:
                p = i - 1
                q = i + 1
            flag = True
            while flag:
                if p >= 0 and q < length and s[p] == s[q]:
                    p -= 1
                    q += 1
                else:
                    p += 1
                    q -= 1
                    if (q - p) > (longest_q - longest_p):
                        longest_p, longest_q = p, q
                    if again:
                        p = i - 1
                        q = i + 1
                        again = False
                    else:
                        flag = False
        return s[longest_p:(longest_q + 1)]
