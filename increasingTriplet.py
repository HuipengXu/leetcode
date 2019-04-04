# @Time    : 2019/4/4 13:50
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
import sys


def increasingTriplet(nums: List[int]) -> bool:
    maximum = minimum = sys.maxsize
    for i in nums:
        if i <= minimum:
            minimum = i
        elif i <= maximum:
            maximum = i
        else:
            return True
    return False


if __name__ == "__main__":
    a = [3, 4, 0, 7, 6]
    print(increasingTriplet(a))
