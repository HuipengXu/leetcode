# @Time    : 2019/6/11 7:58
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def back_tracking(i: int, tmp: List[int], sum_: int) -> None:
            if i == len(candidates) or sum_ >= target:
                if sum_ == target:
                    res.append(tmp)
                return
            back_tracking(i + 1, tmp + [candidates[i]], sum_ + candidates[i])
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            back_tracking(j, tmp, sum_)

        back_tracking(0, [], 0)
        return res

    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def back_tracking(i: int, tmp: List[int], sum_: int) -> None:
            if sum_ == target:
                res.append(tmp)
                return
            for j in range(i, len(candidates)):
                if sum_ + candidates[j] > target: break
                if j - 1 >= i and candidates[j] == candidates[j - 1]: continue
                back_tracking(j + 1, tmp + [candidates[j]], sum_ + candidates[j])

        back_tracking(0, [], 0)
        return res


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 5, 2, 1, 2]
    print(s.combinationSum2(candidates, 5))
