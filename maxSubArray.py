# @Time    : 2019/5/15 21:52
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ret = -float('inf')
        sub_sum = 0
        for i in range(len(nums)):
            if sub_sum < 0:
                sub_sum = nums[i]
            else:
                sub_sum += nums[i]
            ret = max(ret, sub_sum)
        return ret

    # 分治
    def maxSubArray1(self, nums: List[int]) -> int:
        def partition(start, end):
            if end - start <= 1:
                return nums[start], nums[start], nums[start], nums[start]
            mid = start + ((end - start) >> 1)
            l1, r1, m1, s1 = partition(start, mid)
            l2, r2, m2, s2 = partition(mid, end)
            l = max(l1, s1 + l2)
            r = max(r2, r1 + s2)
            m = max(m1, m2, r1 + l2)
            s = s1 + s2
            return l, r, m, s

        _, _, m, _ = partition(0, len(nums))
        return m


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))
    print(s.maxSubArray1(nums))
