# @Time    : 2019/6/15 10:40
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binary_search(nums: List[int]) -> bool:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + ((high - low) >> 1)
                if target == nums[mid]:
                    return True
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        def recur(nums: List[int]) -> bool:
            if not nums: return False
            mid = len(nums) // 2
            if nums[mid] == target:
                return True
            elif nums[0] <= target < nums[mid]:
                return binary_search(nums[:mid])
            elif nums[mid] < target <= nums[-1]:
                return binary_search(nums[mid + 1:])
            else:
                for n in nums:
                    if target == n:
                        return True
                return False

        return recur(nums)

    def search1(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return True
            if nums[mid] == nums[low] == nums[high]:
                low += 1
                high -= 1
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False


if __name__ == '__main__':
    nums = [2, 5, 6, 2, 2, 2, 2]
    s = Solution()
    print(s.search1(nums, 5))
