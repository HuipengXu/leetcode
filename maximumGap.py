# @Time    : 2019/7/13 9:00
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def radix_sort(nums: List[int]) -> None:
            j = len(str(max(nums)))
            i = 0
            while i < j:
                bucket_list = [[] for _ in range(10)]
                for x in nums:
                    bucket_list[(x // 10 ** i) % 10].append(x)
                nums.clear()
                for x in bucket_list:
                    for y in x:
                        nums.append(y)
                i += 1

        radix_sort(nums)
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i - 1])
        return res
