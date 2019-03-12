# @Time    : 2019/3/12 10:22
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

partition_recorder = []
all_partitions = []


def partition(s: str):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    global partition_recorder, all_partitions
    if len(s) == 0:
        all_partitions.append(partition_recorder.copy())
        return
    for i in range(1, len(s) + 1):
        if is_palindrome(s[:i]):
            partition_recorder.append(s[:i])
            partition(s[i:])
            partition_recorder.pop()


def is_palindrome(s: str):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution(object):

    def __init__(self):
        self.partition_recorder = []
        self.all_partitions = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self._partition(s)
        return self.all_partitions

    def _partition(self, s):
        if len(s) == 0:
            self.all_partitions.append(self.partition_recorder.copy())
            return
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                self.partition_recorder.append(s[:i])
                self._partition(s[i:])
                self.partition_recorder.pop()

    def is_palindrome(self, s: str):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = 'khjgfghj'
    so = Solution()
    ret = so.partition(s)
    print(ret)
