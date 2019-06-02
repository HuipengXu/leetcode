# @Time    : 2019/6/2 14:01
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for word in s.split():
            res.append(word[::-1])
        return ' '.join(res)

    def reverseWords1(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())
