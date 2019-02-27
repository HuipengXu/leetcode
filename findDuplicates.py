# @Time    : 2019/2/27 18:15
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


# 过不了
def findDuplicates0(nums: List[int]) -> List[int]:
    if nums is None or len(nums) < 2: return []
    res = []
    for i in range(len(nums)):
        while nums[i] != i + 1:
            if nums[i] == nums[nums[i] - 1]:
                if nums[i] not in res:
                    res.append(nums[i])
                break
            temp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = temp
    return res


# 通过
def findDuplicates1(nums: List[int]) -> List[int]:
    if nums is None or len(nums) < 2: return []
    res = []
    for i in range(len(nums)):
        while nums[i] != i + 1:
            if nums[i] == nums[nums[i] - 1]:
                res.append(nums[i])
                break
            temp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = temp
    return list(set(res))


if __name__ == "__main__":
    test = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDuplicates0(test))
