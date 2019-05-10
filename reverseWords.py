# @Time    : 2019/5/10 15:49
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        return ' '.join(words[::-1])


if __name__ == '__main__':
    ss = "the sky is blue"
    s = Solution()
    print(s.reverseWords(ss))
