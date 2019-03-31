# @Time    : 2019/3/31 18:13
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


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
