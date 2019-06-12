# @Time    : 2019/6/12 12:11
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1]) if words else 0

    def lengthOfLastWord1(self, s: str) -> int:
        length, last = 0, True
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                length += 1
                last = False
            elif s[i].isspace() and not last:
                return length
        return length
