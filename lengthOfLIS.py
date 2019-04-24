# @Time    : 2019/4/24 10:19
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # 满足题目要求的 O(n^2) 的时间复杂度居然也超时，python 简直醉了
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_length = 1
        length = len(nums)
        states = [[-float('inf') for _ in range(length + 1)] for _ in range(length)]
        states[0][1] = nums[0]
        for i in range(1, length):
            for j in range(max_length):
                if states[i - 1][j] < nums[i]:
                    states[i][j + 1] = min(states[i - 1][j + 1], nums[i])
                else:
                    states[i][j + 1] = states[i - 1][j + 1]
            if states[i - 1][max_length] < nums[i]:
                max_length += 1
                states[i][max_length] = nums[i]
        return max_length

    # 通过
    def lengthOfLIS1(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0: return 0
        max_length = 1
        states = [[-float('inf')] for _ in range(length)]
        states[0].append(nums[0])
        for i in range(1, length):
            for j in range(max_length):
                if states[i - 1][j] < nums[i]:
                    states[i].append(min(states[i - 1][j + 1], nums[i]))
                else:
                    states[i].append(states[i - 1][j + 1])
            if states[i - 1][max_length] < nums[i]:
                max_length += 1
                states[i].append(nums[i])
        return max_length

    # 降低空间复杂度
    def lengthOfLIS2(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0: return 0
        max_length = 0
        states = [-float('inf')] * (length + 1)
        for i in range(length):
            for j in range(max_length):
                if states[j] < nums[i]:
                    states[j + 1] = min(states[j + 1], nums[i])
            if states[max_length] < nums[i]:
                max_length += 1
                states[max_length] = nums[i]
        return max_length

    # 二分法
    def lengthOfLIS3(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0: return 0
        max_length = 0
        states = [0] * length
        low = 0
        for num in nums:
            high = max_length
            while low < high:
                mid = low + ((high - low) >> 1)
                if states[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            states[low] = num
            if low == max_length: max_length += 1
        return max_length


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    print(s.lengthOfLIS1(nums))
    print(s.lengthOfLIS2(nums))
    print(s.lengthOfLIS3(nums))
