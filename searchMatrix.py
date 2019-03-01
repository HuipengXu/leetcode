# @Time    : 2019/3/1 11:03
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

"""
搜索二维矩阵 II
https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/261/before-you-start/1108/
"""


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if len(matrix) == 0 or len(matrix[0]) == 0: return False
    width = len(matrix)
    length = len(matrix[0])
    for i in range(width - 1, -1, -1):
        if matrix[i][-1] < target:
            continue
        for j in range(length - 1, -1, -1):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                break
    return False
