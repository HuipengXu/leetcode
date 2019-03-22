# @Time    : 2019/3/21 20:04
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


def word_break_bt(s: str, word_dict: List[str]) -> List[str]:
    sentences = []
    words = []

    def back_tracking(s):
        if len(s) == 0:
            sentence = ' '.join(words).strip()
            sentences.append(sentence)
            return
        for i in range(1, len(s) + 1):
            if s[:i] in word_dict:
                words.append(s[:i])
                back_tracking(s[i:])
                words.pop()

    back_tracking(s)
    return sentences


def word_break_dp(s: str, word_dict: List[str]) -> List[str]:
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    for i in range(1, len(dp)):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = 1
                break

    def recur(i):
        if i == len(s):
            sentence = ' '.join(words).strip()
            sentences.append(sentence)
            return
        for j in range(i + 1, len(s)):
            if dp[j] and s[i:j] in word_dict:
                words.append(s[i:j])
                recur(j)
                words.pop()

    sentences = []
    if dp[len(s)]:
        words = []
        recur(0)
    return sentences


if __name__ == "__main__":
    # s = "pineapplepenapple"
    # word_dict = ['apple', 'pen', 'applepen', 'pine', 'pineapple']
    # s = "catsanddog"
    # word_dict = ["cat", "cats", "and", "sand", "dog"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    # print(word_break_bt(s, word_dict))
    print(word_break_dp(s, word_dict))
