# @Time    : 2019/5/28 16:33
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_zero = cnt_one = cnt_two = 0
        for num in nums:
            if num == 0:
                cnt_zero += 1
            elif num == 1:
                cnt_one += 1
            else:
                cnt_two += 1
        nums[:cnt_zero] = [0] * cnt_zero
        nums[cnt_zero:cnt_zero + cnt_one] = [1] * cnt_one
        nums[cnt_zero + cnt_one:] = [2] * cnt_two

    def sortColors1(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] < 2:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        k = 0
        for i in range(j):
            if nums[i] < 1:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1

    def sortColors2(self, nums: List[int]) -> None:
        cur, low, high = 0, 0, len(nums) - 1
        while cur <= high:
            if nums[cur] == 0:
                nums[cur], nums[low] = nums[low], nums[cur]
                low += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[high] = nums[high], nums[cur]
                high -= 1
            else:
                cur += 1


if __name__ == '__main__':
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0, 2]
    print(s.sortColors2(nums))
    print(nums)
