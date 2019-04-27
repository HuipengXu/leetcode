# @Time    : 2019/4/26 12:11
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import defaultdict, deque


class Solution:
    # 超时
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        def transform(word: str, target: str) -> bool:
            diff = 0
            for w, t in zip(word, target):
                if w != t:
                    diff += 1
            return True if diff == 1 else False

        word_set = set(wordList)
        tree_dict = defaultdict(list)
        children = {beginWord}
        # 构造树
        while children:
            tmp = set()
            for child in children:
                for word in word_set:
                    if word not in tmp and transform(child, word):
                        tree_dict[child].append(word)
                        tmp.add(word)
            for w in tmp: word_set.remove(w)
            children = tmp
        ret = 1
        children = [beginWord]
        # bfs
        while children:
            tmp = []
            for child in children:
                if child == endWord: return ret
                tmp += tree_dict[child]
            ret += 1
            children = tmp
        return 0

    # 还 tm 超时
    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        def transform(word: str, target: str) -> bool:
            diff = 0
            for w, t in zip(word, target):
                if w != t:
                    diff += 1
            return True if diff == 1 else False

        word_set = set(wordList)
        children = {beginWord}
        visited = set()
        ret = 1
        while children:
            tmp = set()
            for child in children:
                for word in word_set:
                    if word not in visited and transform(child, word):
                        if word == endWord: return ret + 1
                        tmp.add(word)
                        visited.add(word)
            children = tmp
            ret += 1
        return 0

    # 参考 http://bookshadow.com/weblog/2015/08/17/leetcode-word-ladder/
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([[beginWord, 1]])
        visited = {beginWord}
        neighbors = defaultdict(list)
        for word in wordList:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x + 1:]
                neighbors[token] += word,
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for x in range(len(word)):
                token = word[:x] + '_' + word[x + 1:]
                for ladder in neighbors[token]:
                    if ladder not in visited:
                        visited.add(ladder)
                        queue += [ladder, length + 1],
        return 0

    # 双端 bfs
    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        begin_queue, end_queue = deque([[beginWord, 1]]), deque([[endWord, 1]])
        begin_length, end_length = {}, {endWord: 1}
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                token = word[:i] + '_' + word[i + 1:]
                neighbors[token].append(word)
        while begin_queue or end_queue:
            if begin_queue:
                word, length = begin_queue.popleft()
                if word in end_length:
                    return length + end_length[word] - 1
                for i in range(len(word)):
                    token = word[:i] + '_' + word[i + 1:]
                    for n in neighbors[token]:
                        if n not in begin_length:
                            begin_length[n] = length + 1
                            begin_queue.append([n, length + 1])
            if end_queue:
                word, length = end_queue.popleft()
                if word in begin_length:
                    return length + begin_length[word] - 1
                for i in range(len(word)):
                    token = word[:i] + '_' + word[i + 1:]
                    for n in neighbors[token]:
                        if n not in end_length:
                            end_length[n] = length + 1
                            end_queue.append([n, length + 1])
        return 0

    # 还是双端 bfs，利用题目信息 全部是小写字母优化查找可转换单词
    def ladderLength4(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        forward, backward = {beginWord}, {endWord}
        wordList = set(wordList)
        letters = ''.join(chr(i) for i in range(ord('a'), ord('a') + 26))
        ret = 1
        while forward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
            cur = set()
            for w in forward:
                for i in range(len(w)):
                    for j in range(26):
                        tmp = w[:i] + letters[j] + w[i + 1:]
                        if tmp in backward:
                            return ret + 1
                        if tmp in wordList:
                            cur.add(tmp)
                            wordList.remove(tmp)
            ret += 1
            forward = cur
        return 0


if __name__ == '__main__':
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]
    s = Solution()
    print(s.ladderLength(beginWord, endWord, wordList))
    print(s.ladderLength1(beginWord, endWord, wordList))
    print(s.ladderLength2(beginWord, endWord, wordList))
    print(s.ladderLength3(beginWord, endWord, wordList))
    print(s.ladderLength4(beginWord, endWord, wordList))
