# @Time    : 2019/5/26 15:54
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from collections import Counter


class Solution:
    # 超时
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def is_repeat(comb: List[int]) -> bool:
            comb_counter = Counter(comb)
            for c in res:
                if Counter(c) == comb_counter: return True
            return False

        def recur(target: int):
            if target < 0: return
            if target == 0 and not is_repeat(combination):
                res.append(combination.copy())
                return
            for num in candidates:
                combination.append(num)
                recur(target - num)
                combination.pop()

        recur(target)
        return res

    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def back_tracking(i: int, tmp_sum: int, tmp: List[int]) -> None:
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            back_tracking(i, tmp_sum + candidates[i], tmp + [candidates[i]])
            back_tracking(i + 1, tmp_sum, tmp)

        back_tracking(0, 0, [])
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def back_tracking(i: int, tmp_sum: int, tmp: List[int]) -> None:
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                back_tracking(j, tmp_sum + candidates[j], tmp + [candidates[j]])

        back_tracking(0, 0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    candidate = [2, 3, 6, 7, 4, 5]
    target = 9
    print(s.combinationSum1(candidate, target))
    print(s.combinationSum2(candidate, target))
