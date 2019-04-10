# @Time    : 2019/4/10 15:15
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def titleToNumber0(self, s: str) -> int:
        ret, length = 0, len(s)
        for i in range(length):
            ret += (ord(s[length - i - 1]) - 64) * 26 ** i
        return ret

    def titleToNumber1(self, s: str) -> int:
        sum = 0
        for l in s:
            sum = sum * 26 + ord(l) - 64
        return sum
