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


def longestPalindrome0(s: str):
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


def longestPalindrome1(s: str):
    """
    动态规划解
    参考：https://segmentfault.com/a/1190000003914228#articleHeader7
    """
    # 初始化状态矩阵
    length = len(s)
    if length in [0, 1]:
        return s
    state = [[0] * length for _ in range(length)]
    max_len = 0
    longest_j = longest_i = 0
    for i in range(length):
        j = i
        while j >= 0:
            if s[i] == s[j] and (i - j < 2 or state[j + 1][i - 1]):
                state[j][i] = 1
                if i - j > max_len:
                    max_len = i - j
                    longest_i, longest_j = i, j
            j -= 1
    return s[longest_j: longest_i + 1]


def longestPalindrome2(s: str) -> str:
    if len(s) == 0: return ''
    states = [[0 for _ in range(j + 1)] for j in range(len(s))]
    states[0][0] = 1
    max_len = 1
    start, end = 0, 1
    for i in range(1, len(s)):
        for j in range(len(states[i - 1])):
            if states[i - 1][j] == 1 and j - 1 >= 0 and s[j - 1] == s[i]:
                states[i][j - 1] = 1
                if i - j + 2 > max_len:
                    max_len = i - j + 2
                    start, end = j - 1, i + 1
        if s[i] == s[i - 1]:
            if max_len < 2:
                max_len = 2
                start, end = i - 1, i + 1
            states[i][i - 1] = 1
        states[i][i] = 1
    return s[start: end]


def longestPalindrome3(s: str) -> str:
    if len(s) == 0: return ''
    start, end = 0, 1

    def expand(left: int, right: int) -> int:
        while (left >= 0 and right < len(s)
               and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        len_ = max(len1, len2)
        if len_ > (end - start):
            start = i - (len_ - 1) // 2
            end = i + len_ // 2 + 1
    return s[start: end]


if __name__ == '__main__':
    ss = "cbbd"
    print(longestPalindrome2(ss))
    print(longestPalindrome3(ss))
