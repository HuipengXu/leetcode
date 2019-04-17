# @Time    : 2019/4/16 9:38
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Tuple, Optional


class Solution:
    def countSmaller0(self, nums: List[int]) -> List[int]:
        """
        归并
        """

        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def countSmaller1(self, nums: List[int]) -> List[int]:
        """
        归并
        """

        def merge_sort_c(enums: List[Tuple[int, int]], start: int, end: int):
            if end - start <= 1: return
            mid = start + ((end - start) >> 1)
            merge_sort_c(enums, start, mid)
            merge_sort_c(enums, mid, end)
            merge(enums, start, mid, end)

        def merge(enums: List[Tuple[int, int]], start: int, mid: int, end: int) -> None:
            i, j, k = mid - 1, end - 1, end - start - 1
            tmp = [(0, 0)] * (end - start)
            while i >= start and j >= mid:
                if enums[i][1] > enums[j][1]:
                    smaller[enums[i][0]] += (j - mid + 1)
                    tmp[k] = enums[i]
                    i -= 1
                else:
                    tmp[k] = enums[j]
                    j -= 1
                k -= 1
            if i < start:
                tmp[:k + 1] = enums[mid: j + 1]
            else:
                tmp[:k + 1] = enums[start:i + 1]
            enums[start: end] = tmp[:]

        enums = list(enumerate(nums))
        smaller = [0] * len(nums)
        merge_sort_c(enums, 0, len(enums))
        return smaller

    def countSmaller2(self, nums: List[int]) -> List[int]:
        """
        树状数组
        """
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = BinaryIndexedTree(len(hashTable)), [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            r[i] = tree.sum(hashTable[nums[i]])
            # 比 nums[i] 大的数都应该加 1
            tree.update(hashTable[nums[i]] + 1, 1)
        return r

    def countSmaller3(self, nums: List[int]) -> List[int]:
        """
        线段树
        """
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = SegmentTree(len(hashTable)), []
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sum(0, hashTable[nums[i]] - 1))
            tree.update(hashTable[nums[i]], 1)
        return r[::-1]

    def countSmaller4(self, nums: List[int]) -> List[int]:
        """
        线段树
        """
        if len(nums) == 0: return []
        hash_table = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree, ret = SegmentTree1(len(hash_table)), [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            ret[i] = tree.sum(hash_table[nums[i]] - 1)
            tree.update(hash_table[nums[i]])
        return ret


class BinaryIndexedTree:
    def __init__(self, n: int):
        self.sums = [0] * (n + 1)

    def update(self, i: int, val: int) -> None:
        while i < len(self.sums):
            self.sums[i] += val
            i += i & -i

    def sum(self, i: int) -> int:
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = start + end >> 1
        root.children = list(filter(None, [
            self.build(start, end)
            for start, end in ((start, mid), (mid + 1, end))]))
        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return root.val

        if i == root.start == root.end:
            root.val += val
            return root.val

        root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0

        if start <= root.start and end >= root.end:
            return root.val

        return sum([self.sum(start, end, c) for c in root.children])


class SegmentTreeNode1:

    def __init__(self, val: int, start: int, end: int,
                 left: Optional['SegmentTreeNode1'] = None,
                 right: Optional['SegmentTreeNode1'] = None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

    def __repr__(self):
        return '<SegmentTreeNode1: {}>'.format(self.val)


class SegmentTree1:

    def __init__(self, n: int):
        self.root = self._build_tree(0, n - 1)

    def _build_tree(self, start: int, end: int) -> Optional[SegmentTreeNode1]:
        if start > end: return
        node = SegmentTreeNode1(0, start, end)
        if start == end: return node
        mid = start + ((end - start) >> 1)
        node.left = self._build_tree(start, mid)
        node.right = self._build_tree(mid + 1, end)
        return node

    def update(self, index: int, node: Optional[SegmentTreeNode1] = None) -> None:
        node = node or self.root
        node.val += 1
        if index == node.start == node.end:
            return
        if index <= node.left.end:
            self.update(index, node.left)
        else:
            self.update(index, node.right)

    def sum(self, index: int, node: Optional[SegmentTreeNode1] = None) -> int:
        node = node or self.root
        if index < node.start: return 0
        if index == node.end: return node.val
        if index <= node.left.end:
            return self.sum(index, node.left)
        else:
            return node.left.val + self.sum(index, node.right)


if __name__ == "__main__":
    num = [8, 5, 4, 6, 7, 2, 1, 2]
    s = Solution()
    print(s.countSmaller0(num))
    print(s.countSmaller1(num))
    print(s.countSmaller3(num))
    print(s.countSmaller4(num))
