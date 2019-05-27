# @Time    : 2019/5/27 18:02
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back_tracking(tmp: List[int], visited: Set[int]):
            if len(tmp) == len(nums):
                res.append(tmp)
                return
            for num in nums:
                if num in visited: continue
                back_tracking(tmp + [num], visited | {num})

        back_tracking([], set())
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))
