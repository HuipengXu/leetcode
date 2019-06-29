# @Time    : 2019/6/29 10:06
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = defaultdict(int)
        for i in range(len(s) - 9):
            count[s[i:i + 10]] += 1
        res = []
        for dna, cnt in count.items():
            if cnt > 1:
                res.append(dna)
        return res

    def findRepeatedDnaSequences1(self, s: str) -> List[str]:
        res, visited = set(), set()
        for i in range(len(s) - 9):
            tmp = s[i:i + 10]
            if tmp in visited:
                res.add(tmp)
            else:
                visited.add(tmp)
        return list(res)

    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        res = []
        count = defaultdict(int)
        for i in range(len(s) - 9):
            tmp = s[i:i + 10]
            count[tmp] += 1
            if count[tmp] == 2:
                res.append(tmp)
        return res
