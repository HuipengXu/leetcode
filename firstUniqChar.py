# @Time    : 2019/3/31 21:18
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import OrderedDict


def first_uniq_char(s: str) -> int:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    index = [s.index(l) for l in letters if s.find(l) != -1 and s.find(l) == s.rfind(l)]
    return min(index) if len(index) > 0 else -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_idxs = OrderedDict()
        for i in range(len(s)):
            if s[i] not in s_idxs:
                s_idxs[s[i]] = [i]
            else:
                s_idxs[s[i]].append(i)
        for _, value in s_idxs.items():
            if len(value) == 1:
                return value[0]
        return -1


if __name__ == "__main__":
    s = 'leetcode'
    print(first_uniq_char(s))
