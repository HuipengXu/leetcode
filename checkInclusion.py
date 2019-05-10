# @Time    : 2019/5/10 8:22
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from collections import defaultdict, Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0: return True
        if len(s2) == 0 or len(s1) > len(s2): return False

        def sum_ascii(s: str) -> int:
            ret = 0
            for alpha in s:
                ret += ord(alpha)
            return ret

        def count(s: str) -> dict:
            cnt = defaultdict(int)
            for c in s:
                cnt[c] += 1
            return cnt

        s1_ascii_sum = sum_ascii(s1)
        s1_count = count(s1)
        sub_s2_ascii_sum = sum_ascii(s2[:len(s1)])
        for i in range(1, len(s2) - len(s1) + 1):
            if s1_ascii_sum == sub_s2_ascii_sum:
                sub_s2_count = count(s2[i - 1: i - 1 + len(s1)])
                if s1_count == sub_s2_count: return True
            sub_s2_ascii_sum = sub_s2_ascii_sum - ord(s2[i - 1]) + ord(s2[i + len(s1) - 1])
        sub_s2_count = count(s2[-len(s1):])
        if s1_ascii_sum == sub_s2_ascii_sum and s1_count == sub_s2_count: return True
        return False

    def checkInclusion1(self, s1: str, s2: str) -> bool:
        if len(s1) == 0: return True
        if len(s2) == 0 or len(s1) > len(s2): return False
        s1_count = Counter(s1)
        sub_s2_count = Counter()
        cnt = 0
        for j in range(len(s1)):
            sub_s2_count[s2[j]] += 1
            if sub_s2_count[s2[j]] == s1_count[s2[j]]:
                cnt += 1
        for i in range(1, len(s2) - len(s1) + 1):
            if cnt == len(s1_count): return True
            if sub_s2_count[s2[i - 1]] == s1_count[s2[i - 1]]:
                cnt -= 1
            sub_s2_count[s2[i - 1]] -= 1
            if sub_s2_count[s2[i - 1]] == 0:
                del sub_s2_count[s2[i - 1]]
            sub_s2_count[s2[i + len(s1) - 1]] += 1
            if sub_s2_count[s2[i + len(s1) - 1]] == s1_count[s2[i + len(s1) - 1]]:
                cnt += 1
        if cnt == len(s1_count): return True
        return False

    # 参考：http://bookshadow.com/weblog/2017/04/30/leetcode-permutation-in-string/
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        c1 = Counter(s1)
        c2 = Counter()
        cnt = 0
        p = q = 0
        while q < l2:
            c2[s2[q]] += 1
            if c1[s2[q]] == c2[s2[q]]:
                cnt += 1
            if cnt == len(c1):
                return True
            q += 1
            if q - p + 1 > l1:
                if c1[s2[p]] == c2[s2[p]]:
                    cnt -= 1
                c2[s2[p]] -= 1
                if c2[s2[p]] == 0:
                    del c2[s2[p]]
                p += 1
        return False


if __name__ == '__main__':
    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"
    s = Solution()
    print(s.checkInclusion(s1, s2))
    print(s.checkInclusion1(s1, s2))
    print(s.checkInclusion2(s1, s2))
