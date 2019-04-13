# @Time    : 2019/4/13 12:26
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def merge_sort_c(nums: list, start: int, end: int) -> None:
            if end - start <= 1: return
            mid = start + ((end - start) >> 1)
            merge_sort_c(nums, start, mid)
            merge_sort_c(nums, mid, end)
            merge(nums, start, mid, end)

        def merge(nums: list, start: int, mid: int, end: int) -> None:
            i, j, k = start, mid, 0
            tmp = [None] * (end - start)
            while i < mid and j < end:
                if ge(nums[i], nums[j]):
                    tmp[k] = nums[i]
                    i += 1
                else:
                    tmp[k] = nums[j]
                    j += 1
                k += 1
            if i == mid:
                while j < end:
                    tmp[k] = nums[j]
                    k += 1
                    j += 1
            else:
                while i < mid:
                    tmp[k] = nums[i]
                    k += 1
                    i += 1
            for m in range(start, end):
                nums[m] = tmp[m - start]

        def ge(num1: int, num2: int) -> bool:
            s1, s2 = str(num1), str(num2)
            if s1 + s2 >= s2 + s1:
                return True
            else:
                return False

        merge_sort_c(nums, 0, len(nums))
        ret = ''.join(str(digit) for digit in nums)
        return '0' if ret[0] == '0' else ret


# 来源于 leetcode
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution1:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        comp = lambda a, b: 1 if a + b < b + a else -1 if a + b > b + a else 0

        return str(int(''.join(sorted([str(x) for x in nums], key=cmp_to_key(comp)))))


if __name__ == "__main__":
    s = Solution()
    a = [0, 0]
    print(s.largestNumber(a))
