# @Time    : 2019/3/31 21:46
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    i, j = 0, len(s) - 1
    while j - i >= 1:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    # s = ["h","e","l","l","o"]
    # s = ["H","a","n","n","a","h"]
    s = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l",
         ":", " ", "P", "a", "n", "a", "m", "a"]
    reverseString(s)
    print(s)
