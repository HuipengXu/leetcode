# @Time    : 2019/5/29 9:40
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import Counter, defaultdict


class Solution:
    # 超时
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if not strs: return res
        cnt = []
        for word in strs:
            word_cnt = Counter(word)
            for i in range(len(res)):
                if len(word) == len(res[i][0]) and word_cnt == cnt[i]:
                    res[i].append(word)
                    break
            else:
                cnt.append(word_cnt)
                res.append([word])
        return res

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            res[tuple(sorted(word))].append(word)
        return list(res.values())

    # 最好解法
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())


if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "atm"]
    print(s.groupAnagrams(strs))
