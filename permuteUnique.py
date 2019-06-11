# @Time    : 2019/6/11 10:36
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Set


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back_tracking(tmp: List[int], path: Set[int]) -> None:
            if len(tmp) == len(nums):
                res.append(tmp)
                return
            visited = set()
            for j in range(len(nums)):
                if j in path or nums[j] in visited: continue
                visited.add(nums[j])
                back_tracking(tmp + [nums[j]], path | {j})

        back_tracking([], set())
        return res

    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def back_tracking(tmp: List[int], path: Set[int]) -> None:
            if len(tmp) == len(nums):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i in path or (i >= 1 and i - 1 not in path and nums[i] == nums[i - 1]): continue
                back_tracking(tmp + [nums[i]], path | {i})

        back_tracking([], set())
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    print(s.permuteUnique(nums))
    print(s.permuteUnique1(nums))
