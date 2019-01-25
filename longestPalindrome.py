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


def longestPalindrome(s: str):
    """
    Manacher 算法
    参考：https://segmentfault.com/a/1190000008484167
    """
    # 重新构造 s 以解决就问题分别讨论
    if len(s) == 0 or len(s) == 1:
        return s

    new_s = ['$#']
    for c in s:
        new_s.append(c)
        new_s.append('#')
    new_s.append('%')
    new_s = ''.join(new_s)

    max_right = id = max_length = 1
    max_i = None
    length = len(new_s)
    p = [1] * length
    for i in range(1, length - 1):
        if i < max_right:
            p[i] = min(p[2 * id - i], max_right - i)
        while new_s[i - p[i]] == new_s[i + p[i]]:
            p[i] += 1
        if p[i] > max_right:
            max_right = i + p[i]
            id = i
        if max_length <= p[i] - 1:
            max_length = p[i] - 1
            max_i = i

    r = int(max_length / 2)
    if max_i % 2:
        center = int(max_i / 2)
        return s[center - r:center + r]
    else:
        center = int((max_i - 2) / 2)
        return s[center - r:center + r + 1]
