# @Time    : 2019/4/15 20:12
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/
from typing import List


class Solution:
    def findDuplicate0(self, nums: List[int]) -> int:
        """
        二分法，不断缩小查找数值范围，而不是缩小数组
        """
        l, r = 1, len(nums) - 1
        while l < r:
            m = l + ((r - l) >> 1)
            cnt = 0
            for num in nums:
                if num <= m:
                    cnt += 1
            if cnt > m:
                r = m
            else:
                l = m + 1
        return l

    def findDuplicate1(self, nums: List[int]) -> int:
        """
        快慢指针
        相关解释：https://blog.csdn.net/u012482487/article/details/49798169
                 http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/
        """
        p = q = 0
        while 1:
            p = nums[p]
            q = nums[nums[q]]
            if p == q:
                break
        q = 0
        while p != q:
            p = nums[p]
            q = nums[q]
        return p


if __name__ == "__main__":
    a = [2, 1, 4, 6, 5, 3, 4, 7]
    s = Solution()
    print(s.findDuplicate1(a))
