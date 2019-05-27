# @Time    : 2019/5/27 19:39
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Set


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if not nums: return res

        def back_tracking(i: int, cur: Set[int]):
            if len(cur) == len(nums): return
            for j in range(i + 1, len(nums)):
                if nums[j] not in cur:
                    tmp = cur | {nums[j]}
                    res.append(list(tmp))
                    back_tracking(j, tmp)

        for i in range(len(nums)):
            res.append([nums[i]])
            back_tracking(i, {nums[i]})
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            tmp = []
            for sub in res:
                tmp.append(sub + [nums[i]])
            res.extend(tmp)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if not nums: return res

        def back_tracking(i: int, cur: List[int]):
            if len(cur) == len(nums): return
            for j in range(i + 1, len(nums)):
                tmp = cur + [nums[j]]
                res.append(tmp)
                back_tracking(j, tmp)

        for i in range(len(nums)):
            res.append([nums[i]])
            back_tracking(i, [nums[i]])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.subsets(nums))
    print(s.subsets2(nums))
