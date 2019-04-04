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
    i, j = len(matrix) - 1, len(matrix[0]) - 1
    j_border = 0
    while i >= 0 and j_border < len(matrix[0]):
        if target < matrix[i][j]:
            j -= 1
            if j < j_border:
                j = len(matrix[0]) - 1
                i -= 1
        elif target > matrix[i][j]:
            j_border = j + 1
            j = len(matrix[0]) - 1
            i -= 1
        else:
            return True
    return False
