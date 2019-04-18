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


if __name__ == '__main__':
    ss = 'aaabb'
    s = Solution()
    print(s.longestSubstring0(ss, 2))
    print(s.longestSubstring2(ss, 2))
