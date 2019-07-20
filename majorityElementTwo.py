# @Time    : 2019/7/20 13:13
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


def radix_sort(nums):
    n = len(str(max(nums)))
    for i in range(n):
        buckets = [[] for _ in range(10)]
        for num in nums:
            idx = num // 10 ** i % 10
            buckets[idx].append(num)
        nums.clear()
        for x in buckets:
            for y in x:
                nums.append(y)


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = n = None
        m_count = n_count = None
        for num in nums:
            if num == m:
                m_count += 1
            elif num == n:
                n_count += 1
            elif not m_count:
                m, m_count = num, 1
            elif not n_count:
                n, n_count = num, 1
            else:
                m_count -= 1
                n_count -= 1
        m_count = n_count = 0
        for num in nums:
            if num == m:
                m_count += 1
            elif num == n:
                n_count += 1
        return [num for num, c in zip((m, n), (m_count, n_count)) if c > len(nums) // 3]


if __name__ == '__main__':
    nums = [5, 5, 5, 5, 1, 2, 3, 4]
    s = Solution()
    print(s.majorityElement(nums))
