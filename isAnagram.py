# @Time    : 2019/3/31 18:16
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from collections import defaultdict

"""
错误理解题意，想得太复杂；下面的解法是，对一个单词的任意一个字母进行移动得到单词为字母异位词的判断。
大概思路是循环拿掉 t 里的每个字母，同时拿掉 s 里同样的字母，将剩余的进行比较，若相同则为异位词
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    if len(s) == 0: return True
    s_idxs = defaultdict(list)
    for i in range(len(s)):
        s_idxs[s[i]].append(i)
    for j in range(len(t)):
        tmp_t = t[:j] + t[j + 1:]
        for idx in s_idxs[t[j]]:
            tmp_s = s[:idx] + s[idx + 1:]
            if tmp_s == tmp_t:
                return True
    return False


"""
242. 有效的字母异位词
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if len(s) == 0: return True
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for i in s:
            s_count[i] += 1
        for j in t:
            t_count[j] += 1
        for key in s_count.keys():
            if s_count[key] != t_count[key]:
                return False
        return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(is_anagram(s, t))
