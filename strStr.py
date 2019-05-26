# @Time    : 2019/5/26 20:10
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(haystack) - i < len(needle): return -1
                k, j = i, 0
                while haystack[k] == needle[j]:
                    k += 1
                    j += 1
                    if j >= len(needle): return i
        return -1
