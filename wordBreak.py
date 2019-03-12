# @Time    : 2019/3/12 19:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


# 回溯法，时间复杂度过高
def wordBreak0(s: str, wordDict: List[str]) -> bool:
    break_ = False

    def _wordBreak(s: str, wordDict: List[str]):
        nonlocal break_
        if break_: return
        if len(s) == 0:
            break_ = True
            return
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                _wordBreak(s[i:], wordDict)

    _wordBreak(s, wordDict)
    return break_


def isin_wordDict(s: str, wordDict: List[str]) -> bool:
    for word in wordDict:
        if s == word:
            return True
    return False


def wordBreak1(s: str, wordDict: List[str]) -> bool:
    break_idx = [0]
    for i in range(len(s) + 1):
        for j in break_idx:
            if isin_wordDict(s[j: i], wordDict):
                break_idx.append(i)
                break
    if break_idx[-1] == len(s):
        return True
    return False


if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    print(len(s))
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(wordBreak1(s, wordDict))
