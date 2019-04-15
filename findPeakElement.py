# @Time    : 2019/4/15 16:10
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import sys
from typing import List


class Solution:
    def findPeakElement0(self, nums: List[int]) -> int:
        j = 0
        pre = -sys.maxsize
        while j < len(nums):
            next_ = nums[j + 1] if j + 1 < len(nums) else -sys.maxsize
            if nums[j] <= pre:
                j += 1
                pre = nums[j]
                continue
            if nums[j] <= next_:
                j += 1
                continue
            return j

    # 为什么二分查找大的那一半一定会有峰值呢？（即nums[mid] < nums[mid + 1]
    # 时，mid + 1
    # ~N一定存在峰值） 我的理解是，首先已知
    # nums[mid + 1] > nums[mid]，那么mid + 2
    # 只有两种可能，一个是大于mid + 1，一个是小于mid + 1，小于mid + 1
    # 的情况，那么mid + 1
    # 就是峰值，大于mid + 1
    # 的情况，继续向右推，如果一直到数组的末尾都是大于的，那么可以肯定最后一个元素是峰值，因为nums[nums.length] = 负无穷
    # 摘自：https://leetcode-cn.com/problems/find-peak-element/comments/，swordjoinmagic 的评论
    def findPeakElement1(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start != end:
            if nums[start] > nums[start + 1]: return start
            if nums[end] > nums[end - 1]: return end
            mid = start + ((end - start) >> 1)
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
                continue
            if nums[mid] < nums[mid - 1]:
                end = mid - 1
                continue
            return mid
        return start


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]
    s = Solution()
    print(s.findPeakElement1(nums))
