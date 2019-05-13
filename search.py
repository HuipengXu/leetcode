# @Time    : 2019/5/12 19:35
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # O(n) 时间内找出旋转点
    def search(self, nums: List[int], target: int) -> int:
        rotate = len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                rotate = i - 1
                break
        if target > nums[0]:
            low, high = 0, rotate
        elif target < nums[0]:
            low, high = rotate + 1, len(nums) - 1
        else:
            return 0
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        if low > high: return -1
        return low

    # 先用二分找出旋转点
    def search1(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        rotate = len(nums) - 1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                rotate = mid
                break
            elif nums[low] <= nums[mid]:
                low = mid + 1
            elif nums[low] > nums[mid]:
                high = mid - 1
        if target > nums[0]:
            low, high = 0, rotate
        elif target < nums[0]:
            low, high = rotate + 1, len(nums) - 1
        else:
            return 0
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        if low > high: return -1
        return low

    def search2(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3]
    target = 0
    print(s.search(nums, target))
    print(s.search1(nums, target))
    print(s.search2(nums, target))
