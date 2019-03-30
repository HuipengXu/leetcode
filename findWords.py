# @Time    : 2019/3/30 20:10
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'children': [None] * 26, 'is_ending': False}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if node['children'][idx] is None:
                new_node = {'children': [None] * 26, 'is_ending': False}
                node['children'][idx] = new_node
            node = node['children'][idx]
        node['is_ending'] = True

    def _end_node(self, word) -> tuple:
        node = self.root
        flag = True
        for letter in word:
            idx = ord(letter) - ord('a')
            if node['children'][idx] is None:
                flag = False
                break
            node = node['children'][idx]
        return node, flag

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node, flag = self._end_node(word)
        return node['is_ending'] if flag else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        _, flag = self._end_node(prefix)
        return flag


class Solution:

    def build_trie(self, words: List[str]) -> Trie:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.build_trie(words)
        row, col = len(board), len(board[0])
        ret = []

        def back_tracking(i: int, j: int):
            coordinates.append((i, j))
            letters.append(board[i][j])
            word = ''.join(letters)
            if not trie.startsWith(word):
                return
            if i > 0 and (i - 1, j) not in coordinates:
                back_tracking(i - 1, j)
                letters.pop()
                coordinates.pop()
            if i < row - 1 and (i + 1, j) not in coordinates:
                back_tracking(i + 1, j)
                letters.pop()
                coordinates.pop()
            if j > 0 and (i, j - 1) not in coordinates:
                back_tracking(i, j - 1)
                letters.pop()
                coordinates.pop()
            if j < col - 1 and (i, j + 1) not in coordinates:
                back_tracking(i, j + 1)
                letters.pop()
                coordinates.pop()
            if trie.search(word):
                if word not in ret:
                    ret.append(word)
                return

        for i in range(row):
            for j in range(col):
                letters = []
                coordinates = []
                back_tracking(i, j)
        return ret


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    # board = [["a","a"]]
    # words = ["aaa"]
    sol = Solution()
    ret = sol.find_words(board, words)
    print(ret)
