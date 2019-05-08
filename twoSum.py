# @Time    : 2019/5/8 9:45
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    # 先记录索引并排序，然后从两端搜索，时间复杂度为 O(nlogn)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s, t = 0, len(nums) - 1
        if t < 0: return []
        num_idxs = sorted(enumerate(nums), key=lambda t: t[1])
        while s != t:
            tmp = num_idxs[s][1] + num_idxs[t][1]
            if tmp == target:
                return [num_idxs[s][0], num_idxs[t][0]]
            elif tmp > target:
                t -= 1
            else:
                s += 1
        return []

    # 利用字典， 时间复杂度最好为 O(n)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for i in range(len(nums)):
            if target - nums[i] in idxs:
                return [idxs[target - nums[i]], i]
            else:
                idxs[nums[i]] = i
        return []
