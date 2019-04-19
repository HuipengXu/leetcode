# @Time    : 2019/4/18 15:27
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import Counter
import re


class Solution:
    def longestSubstring0(self, s: str, k: int) -> int:
        def recur(s: str, length: int = 0):
            if len(s) < k: return 0
            count_dict = {}
            for i in range(len(s)):
                if s[i] not in count_dict:
                    count_dict[s[i]] = [1, [i]]
                else:
                    count_dict[s[i]][0] += 1
                    count_dict[s[i]][1].append(i)
            filters = [idx for cnt, indexes in count_dict.values() if cnt < k for idx in indexes]
            if len(filters) == 0:
                if len(s) > length: length = len(s)
                return length
            filters.append(len(s))
            start = 0
            for i in filters:
                l = recur(s[start:i], length)
                start = i + 1
                if l > length: length = l
            return length

        return recur(s)

    def longestSubstring1(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        for ch in s:
            if s.count(ch) < k:
                return max(self.longestSubstring1(sub, k)
                           for sub in s.split(ch))
        return len(s)

    def longestSubstring2(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        cnt = Counter(s)
        filters = [ch for ch in cnt if cnt[ch] < k]
        if not filters: return len(s)
        tokens = re.split('|'.join(filters), s)
        return max(self.longestSubstring2(token, k) for token in tokens)

    # 时间复杂度为 O(n)，外层只会循环 26 次，内层要么是 i 要么是 j 增加 1，所以最多 2n，故最糟糕的情况为 O(52n)
    # 来自 https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87739/Java-Strict-O(N)-Two-Pointer-Solution
    def longestSubString3(self, s: str, k: int) -> int:
        max_length = 0
        for h in range(1, 27):
            counts = [0] * 26
            i = j = unique = no_less_than_k = 0
            while j < len(s):
                if unique <= h:
                    idx = ord(s[j]) - ord('a')
                    if counts[idx] == 0:
                        unique += 1
                    counts[idx] += 1
                    if counts[idx] == k:
                        no_less_than_k += 1
                    j += 1
                else:
                    idx = ord(s[i]) - ord('a')
                    if counts[idx] == k:
                        no_less_than_k -= 1
                    counts[idx] -= 1
                    if counts[idx] == 0:
                        unique -= 1
                    i += 1
                if unique == h and no_less_than_k == unique:
                    max_length = max(j - i, max_length)
        return max_length


if __name__ == '__main__':
    ss = 'sahgdjgjd'
    s = Solution()
    print(s.longestSubstring0(ss, 2))
    print(s.longestSubstring2(ss, 2))
    print(s.longestSubString3(ss, 2))
