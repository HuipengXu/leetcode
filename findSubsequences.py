# @Time    : 2019/7/11 20:49
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        idx_map = {nums[0]: -1}
        for i in range(1, len(nums)):
            if nums[i] not in idx_map:
                idx_map[nums[i]] = len(res)
                res += [lst + [nums[i]] for lst in res if lst[-1] <= nums[i]] + [[nums[i]]]
            else:
                tmp = len(res)
                res += [res[j] + [nums[i]] for j in range(tmp) if res[j][-1] <= nums[i] and j >= idx_map[nums[i]]]
                idx_map[nums[i]] = tmp
        return [lst for lst in res if len(lst) > 1]

    # 超时
    def findSubsequences1(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back_tracking(i: int, tmp: List[int]) -> None:
            if len(tmp) > 1 and tmp not in res:
                res.append(tmp)
            for j in range(i, len(nums)):
                if not tmp or tmp[-1] <= nums[j]:
                    back_tracking(j + 1, tmp + [nums[j]])

        back_tracking(0, [])
        return res

    def findSubsequences2(self, nums: List[int]) -> List[List[int]]:
        """trie"""
        trie = {}

        def insert(dic: dict, num: int):
            for k, v in dic.items():
                if k <= num:
                    insert(v, num)
            if num not in dic:
                dic[num] = {}

        for num in nums:
            insert(trie, num)

        res = []

        def traverse(dic: dict, tmp: List[int]):
            if len(tmp) > 1: res.append(tmp)
            for prefix, children in dic.items():
                traverse(children, tmp + [prefix])

        traverse(trie, [])

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(s.findSubsequences(nums))
    print(s.findSubsequences1(nums))
    print(s.findSubsequences2(nums))
