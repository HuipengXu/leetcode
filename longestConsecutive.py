# @Time    : 2019/4/19 14:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length_dict = {}
        max_length = 0
        for num in nums:
            if num not in length_dict:
                left = length_dict.get(num - 1, 0)
                right = length_dict.get(num + 1, 0)
                current = left + right + 1
                max_length = max(current, max_length)
                length_dict[num - left] = current
                length_dict[num + right] = current
                length_dict[num] = current
        return max_length

    # O(n) 时间复杂度，外层循环只有能进入 if 的只有孤立的值和序列的最大值，实际上加上内层的 while 循环，总循环次数基本等于 n
    def longestConsecutive1(self, nums: List[int]) -> int:
        nums = set(nums)
        ret = 0
        for i in nums:
            if i + 1 not in nums:
                next_ = i - 1
                while next_ in nums:
                    next_ -= 1
                ret = max(ret, i - next_)
        return ret

    def longestConsecutive2(self, nums: List[int]) -> int:
        length = len(nums)
        uf = UnionFind(length)
        dt = {}
        for i in range(length):
            if nums[i] in dt: continue
            dt[nums[i]] = i
            if nums[i] - 1 in dt:
                uf.union(i, dt[nums[i] - 1])
            if nums[i] + 1 in dt:
                uf.union(i, dt[nums[i] + 1])
        return uf.max_size


class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.max_size = 1

    def union(self, p: int, q: int) -> None:
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return
        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
            self.max_size = max(self.max_size, self.size[root_q])
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
            self.max_size = max(self.max_size, self.size[root_p])

    def find(self, p: int):
        if self.parent[p] == p: return p
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]


if __name__ == '__main__':
    nums = [4, 1, 7, 6, 10, 3, 1, 2]
    s = Solution()
    print(s.longestConsecutive(nums))
    print(s.longestConsecutive1(nums))
    print(s.longestConsecutive2(nums))
