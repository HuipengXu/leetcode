# 213. 打家劫舍 II


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)

    if length < 3:
        return 0

    if length == 3:
        return max(nums)

    nums_and_index = [c for c in enumerate(nums)]
    nums_and_index.sort(key=lambda c: c[1], reverse=True)


nums = [1, 2, 3, 1]
print(rob(nums))
