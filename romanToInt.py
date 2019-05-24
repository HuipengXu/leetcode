# @Time    : 2019/5/24 20:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def romanToInt(self, s: str) -> int:
        res = i = 0
        roman_hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i < len(s):
            if i + 1 < len(s) and roman_hash[s[i]] < roman_hash[s[i + 1]]:
                res += roman_hash[s[i + 1]] - roman_hash[s[i]]
                i += 2
            else:
                res += roman_hash[s[i]]
                i += 1
        return res
