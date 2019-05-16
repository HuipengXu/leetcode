# @Time    : 2019/5/16 19:30
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + ((high - low) >> 1)
            if mid ** 2 > x:
                high = mid - 1
            elif mid ** 2 < x:
                if (mid + 1) ** 2 > x:
                    return mid
                low = mid + 1
            else:
                return mid

    def mySqrt1(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + ((high - low) >> 1)
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(257))
