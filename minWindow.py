# @Time    : 2019/6/3 14:22
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ''
        t_counter = Counter(t)
        lookup = Counter()
        left = right = 0
        res, length = '', float('inf')
        while right < len(s):
            lookup[s[right]] += 1
            while all(map(lambda x: t_counter[x] <= lookup[x], t_counter.keys())):
                if right - left + 1 < length:
                    res = s[left:right + 1]
                    length = right - left + 1
                lookup[s[left]] -= 1
                left += 1
            right += 1
        return res

    # 超出时间限制
    def minWindow1(self, s: str, t: str) -> str:
        if not s or not t: return ''
        t_counter = [0] * 128
        for letter in t:
            t_counter[ord(letter)] += 1
        lookup = [0] * 128
        left = right = 0
        res, length = '', float('inf')
        while right < len(s):
            lookup[ord(s[right])] += 1
            while all(map(lambda x: t_counter[ord(x)] <= lookup[ord(x)], set(t))):
                if right - left + 1 < length:
                    res = s[left:right + 1]
                    length = right - left + 1
                if lookup[ord(s[left])] > 0:
                    lookup[ord(s[left])] -= 1
                left += 1
            right += 1
        return res

    def minWindow2(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res


if __name__ == '__main__':
    s = Solution()
    s1 = 'BBBC'
    t = 'BC'
    print(s.minWindow2(s1, t))
