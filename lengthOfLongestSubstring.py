# @Time    : 2019/5/9 15:04
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        states = [i for i in range(len(s))]
        max_len = 1
        for i in range(1, len(s)):
            j = i - 1
            while j >= states[i - 1]:
                if s[i] == s[j]:
                    break
                j -= 1
            states[i] = j + 1
            max_len = max(max_len, i - j)
        return max_len

    # https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/comments/
    def lengthOfLongestSubstring1(self, s: str) -> int:
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans

    # 滑动窗口
    def lengthOfLongestSubstring2(self, s: str) -> int:
        i = j = 0
        ans = 0
        window = set()
        while i < len(s) and j < len(s):
            if s[j] in window:
                window.remove(s[i])
                i += 1
            else:
                window.add(s[j])
                j += 1
                ans = max(ans, j - i)
        return ans


if __name__ == '__main__':
    ss = "abcabcbb"
    s = Solution()
    print(s.lengthOfLongestSubstring(ss))
    print(s.lengthOfLongestSubstring1(ss))
    print(s.lengthOfLongestSubstring2(ss))
